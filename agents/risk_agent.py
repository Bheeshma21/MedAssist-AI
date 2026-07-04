def predict_risk(patient_data, medical_context, drug_warnings):

    score = 0
    reasons = []
    possible_conditions = []

    symptoms = [s.lower() for s in patient_data.get("symptoms", [])]

    medical_history = [
        h.lower() for h in patient_data.get("medical_history", [])
    ]

    family_history = [
        h.lower() for h in patient_data.get("family_history", [])
    ]

    social_history = [
        h.lower() for h in patient_data.get("social_history", [])
    ]

    red_flags = [
        r.lower() for r in patient_data.get("red_flags", [])
    ]

    context = medical_context.get(
        "medical_context",
        ""
    ).lower()

    # ----------------------------------------
    # Symptoms
    # ----------------------------------------

    symptom_scores = {
        "chest pain": 4,
        "shortness of breath": 4,
        "breathlessness": 4,
        "orthopnea": 3,
        "leg swelling": 2,
        "fatigue": 1,
        "fever": 1,
        "cough": 1,
    }

    for symptom, value in symptom_scores.items():

        if symptom in symptoms:

            score += value
            reasons.append(f"Symptom: {symptom}")

    # ----------------------------------------
    # Red Flags
    # ----------------------------------------

    for flag in red_flags:

        score += 2
        reasons.append(f"Red Flag: {flag}")

    # ----------------------------------------
    # Past Medical History
    # ----------------------------------------

    history_scores = {
        "previous myocardial infarction": 3,
        "myocardial infarction": 3,
        "heart failure": 3,
        "hypertension": 1,
        "diabetes": 1,
        "copd": 2,
    }

    for disease, value in history_scores.items():

        if disease in medical_history:

            score += value
            reasons.append(f"Past Medical History: {disease}")

    # ----------------------------------------
    # Family History
    # ----------------------------------------

    if family_history:

        score += 1
        reasons.append("Relevant family history")

    # ----------------------------------------
    # Smoking
    # ----------------------------------------

    for history in social_history:

        if "smoker" in history:

            score += 1
            reasons.append("Smoking history")

    # ----------------------------------------
    # Drug Interaction
    # ----------------------------------------

    if drug_warnings:

        score += 2
        reasons.append("Potential high-risk drug interaction")

    # ----------------------------------------
    # RAG Evidence
    # ----------------------------------------

    evidence_map = {
        "heart failure": "Heart Failure",
        "pneumonia": "Pneumonia",
        "copd": "COPD",
        "pulmonary embolism": "Pulmonary Embolism",
        "myocardial infarction": "Myocardial Infarction",
    }

    for keyword, condition in evidence_map.items():

        if keyword in context:

            possible_conditions.append(condition)

    possible_conditions = list(dict.fromkeys(possible_conditions))

    # ----------------------------------------
    # Risk Classification
    # ----------------------------------------

    if score >= 10:

        risk = "EMERGENCY"

        action = (
            "Immediate emergency evaluation should be considered."
        )

    elif score >= 7:

        risk = "HIGH"

        action = (
            "Urgent medical evaluation is recommended."
        )

    elif score >= 4:

        risk = "MODERATE"

        action = (
            "Prompt clinical assessment is recommended."
        )

    else:

        risk = "LOW"

        action = (
            "Routine clinical follow-up is appropriate."
        )

    return {

        "risk_level": risk,

        "risk_score": score,

        "possible_conditions": possible_conditions,

        "reasons": reasons,

        "recommended_action": action

    }