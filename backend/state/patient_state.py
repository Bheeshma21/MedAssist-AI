from typing import TypedDict


class PatientState(TypedDict, total=False):

    conversation: str

    patient_data: dict

    supervisor: dict

    medical_context: dict

    drug_warnings: list

    risk_report: dict

    confidence_report: dict

    soap_note: str

    explanation_report: str

    safety_report: dict

    guardrail_report: dict

    final_response: dict