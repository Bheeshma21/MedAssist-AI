def calculate_confidence(patient_data, risk_report):

    score = 0

    symptoms = [s.lower() for s in patient_data.get("symptoms", [])]

    history = [h.lower() for h in patient_data.get("medical_history", [])]

    # Strong symptoms
    if "orthopnea" in symptoms:
        score += 20

    if "leg swelling" in symptoms:
        score += 20

    if "breathlessness" in symptoms:
        score += 15

    if "fatigue" in symptoms:
        score += 10

    # Medical history
    if "heart attack" in " ".join(history):
        score += 20

    if "hypertension" in " ".join(history):
        score += 10

    if "diabetes" in " ".join(history):
        score += 5

    score = min(score, 100)

    return {
        "confidence": score,
        "level": (
            "Very High" if score >= 85
            else "High" if score >= 70
            else "Moderate" if score >= 50
            else "Low"
        )
    }