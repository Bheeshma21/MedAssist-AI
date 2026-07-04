import json
import time
from google.genai.errors import ServerError
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
prompt = ChatPromptTemplate.from_template("""
You are an experienced clinical documentation assistant.

Your task is to extract ONLY the clinical information that is explicitly mentioned in the doctor-patient conversation.

IMPORTANT RULES

1. Do NOT guess or infer information.
2. Do NOT invent diagnoses.
3. If a field is not mentioned, return an empty string "" or an empty list [].
4. Return ONLY valid JSON.
5. Do not use Markdown.
6. Preserve the patient's wording whenever possible.

Extract the following fields:

- chief_complaint
- history_present_illness
- symptoms
- duration
- medical_history
- medications
- allergies
- family_history
- social_history
- red_flags

Definitions:

chief_complaint:
The primary reason the patient is seeking medical care.

history_present_illness:
A concise summary of the current illness.

symptoms:
List every symptom explicitly mentioned.

duration:
Duration of the illness if stated.

medical_history:
Previous diseases or chronic conditions.
Examples:
- Hypertension
- Diabetes
- Asthma
- COPD
- Heart Failure
- Previous Myocardial Infarction

medications:
Current medications.

allergies:
Drug or environmental allergies.

family_history:
Any illness mentioned in close family members.

social_history:
Smoking, alcohol, occupation, recreational drugs, living situation, exercise.

red_flags:
Only include clinically important findings explicitly mentioned, such as:
- Chest pain
- Progressive shortness of breath
- Orthopnea
- Leg swelling
- Hemoptysis
- Syncope
- Severe bleeding
- High fever
- Altered mental status

Return EXACTLY this JSON:

{{
    "chief_complaint": "",
    "history_present_illness": "",
    "symptoms": [],
    "duration": "",
    "medical_history": [],
    "medications": [],
    "allergies": [],
    "family_history": [],
    "social_history": [],
    "red_flags": []
}}

Conversation:
{conversation}
""")
chain = prompt | llm


def extract_symptoms(conversation):

    response = None

    for attempt in range(3):

        try:
            response = chain.invoke({
                "conversation": conversation
            })
            break

        except ServerError:
            print(f"Gemini busy... Retry {attempt + 1}/3")
            time.sleep(5)

    if response is None:
        raise Exception("Gemini service unavailable after 3 retries.")

    json_text = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(json_text)

    except json.JSONDecodeError:
        print("Invalid JSON returned by Gemini.")

        return {
            "chief_complaint": "",
            "history_present_illness": "",
            "symptoms": [],
            "duration": "",
            "medical_history": [],
            "medications": [],
            "allergies": [],
            "family_history": [],
            "social_history": [],
            "red_flags": []
        }