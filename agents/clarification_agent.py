REQUIRED_FIELDS = {
    "chest pain": [
        "When did the pain start?",
        "Where is the pain located?",
        "Does the pain spread to the arm or jaw?",
        "Are you sweating?",
        "Do you have shortness of breath?"
    ],

    "fever": [
        "What is your temperature?",
        "How many days have you had fever?",
        "Any cough?",
        "Any sore throat?"
    ],

    "headache": [
        "When did it start?",
        "How severe is it?",
        "Do you have vomiting?",
        "Any blurred vision?"
    ]
}


def get_clarification_questions(symptoms):

    questions = []

    for symptom in symptoms:

        symptom = symptom.lower()

        if symptom in REQUIRED_FIELDS:
            questions.extend(REQUIRED_FIELDS[symptom])

    return list(dict.fromkeys(questions))