def safety_review(patient_data, drug_warnings, soap_note):
    warnings = []

    if drug_warnings:
        warnings.append(
            "Potential drug interaction detected."
        )

    if not patient_data.get("symptoms"):
        warnings.append(
            "No symptoms were extracted."
        )

    if "Plan:" not in soap_note:
        warnings.append(
            "SOAP note is missing a treatment plan."
        )

    return {
        "safe": len(warnings) == 0,
        "warnings": warnings
    }