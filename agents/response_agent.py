class ResponseAgent:

    def build(self, state):

        return {
            "patient_data": state.get("patient_data", {}),
            "risk_report": state.get("risk_report", {}),
            "drug_warnings": state.get("drug_warnings", []),
            "soap_note": state.get("soap_note", ""),
            "confidence_report": state.get("confidence_report", {}),
            "safety_report": state.get("safety_report", {}),
            "explanation_report": state.get("explanation_report", ""),
            "guardrail_report": state.get("guardrail_report", {})
        }


response_agent = ResponseAgent()