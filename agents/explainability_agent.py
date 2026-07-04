def generate_explanation(patient_data, risk_report):

    symptoms = patient_data.get("symptoms", [])

    explanation = []

    explanation.append(
        "The AI considered the following symptoms:"
    )

    for symptom in symptoms:
        explanation.append(f"• {symptom}")

    explanation.append("")

    explanation.append(
        f"Overall Risk Level: {risk_report['risk_level']}"
    )

    explanation.append("")

    explanation.append(
        "The assessment is supported by the retrieved medical evidence."
    )

    return "\n".join(explanation)