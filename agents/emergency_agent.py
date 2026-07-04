EMERGENCY_KEYWORDS = [
    "chest pain",
    "loss of consciousness",
    "severe bleeding",
    "stroke",
    "difficulty breathing",
    "seizure"
]


def check_emergency(symptoms):

    found = []

    symptoms = [s.lower() for s in symptoms]

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in symptoms:
            found.append(keyword)

    return {
        "emergency": len(found) > 0,
        "matched": found
    }