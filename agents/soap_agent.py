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

Your task is to generate a professional SOAP Note from the provided patient information.

IMPORTANT RULES

1. Use ONLY the information provided.
2. Do NOT invent symptoms, medical history, medications, allergies, or examination findings.
3. If information is unavailable, write "Not available."
4. Do NOT make definitive diagnoses.
5. In the Assessment section, use cautious clinical language such as:
   - "The findings are suggestive of..."
   - "The presentation is consistent with..."
   - "Differential diagnoses include..."
   - "Clinical confirmation requires further evaluation."
6. Never state that a disease is confirmed unless explicitly provided.
7. Use the retrieved medical context only to support clinical reasoning, not to introduce new patient facts.
8. Mention drug interaction warnings only if they are provided.
9. Keep the note concise, professional, and suitable for clinician review.

Patient Information:
{patient_data}

Retrieved Medical Context:
{medical_context}

Drug Interaction Warnings:
{drug_warnings}

Generate the SOAP Note using exactly this format:

Subjective:
- Chief Complaint
- History of Present Illness
- Relevant Medical History
- Current Medications
- Allergies
- Family History
- Social History

Objective:
- Available examination findings
- Available investigations
- If unavailable, state "Not available."

Assessment:
- Summarize the clinical presentation.
- State the most likely clinical impression using cautious language.
- Include 2–4 differential diagnoses if supported by the available evidence.
- Clearly mention that confirmation requires further clinical evaluation and investigations.

Plan:
- Recommended investigations
- Initial management recommendations
- Lifestyle advice (if applicable)
- Follow-up recommendations
- Drug interaction warnings (if any)

Return ONLY the SOAP Note.
""")
chain = prompt | llm

def generate_soap_note(patient_data, medical_context, drug_warnings):

    response = chain.invoke({
        "patient_data": patient_data,
        "medical_context": medical_context["medical_context"],
        "drug_warnings": drug_warnings
    })

    return response.content