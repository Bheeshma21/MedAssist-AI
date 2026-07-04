def validate_response(result):

    warnings = []

    if not result.get("medical_context"):
        warnings.append(
            "No medical evidence retrieved."
        )

    if not result.get("risk_report"):
        warnings.append(
            "Risk assessment missing."
        )

    if not result.get("soap_note"):
        warnings.append(
            "SOAP Note missing."
        )

    return {
        "passed": len(warnings) == 0,
        "warnings": warnings
    }