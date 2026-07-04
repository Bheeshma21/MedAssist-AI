from typing import TypedDict


class GraphState(TypedDict, total=False):

    # ===========================
    # User Input
    # ===========================
    conversation: str
    role: str
    session_id: str

    # ===========================
    # Extracted Information
    # ===========================
    patient_data: dict

    # ===========================
    # Supervisor Decision
    # ===========================
    supervisor: dict

    # ===========================
    # Medical Knowledge
    # ===========================
    medical_context: dict

    # ===========================
    # Drug Safety
    # ===========================
    drug_warnings: list

    # ===========================
    # Clinical Reports
    # ===========================
    risk_report: dict

    confidence_report: dict

    soap_note: str

    explanation_report: str

    safety_report: dict

    guardrail_report: dict

    # ===========================
    # Final Response
    # ===========================
    final_response: dict

    # ===========================
    # Errors
    # ===========================
    error: str