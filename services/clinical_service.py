from agents.symptom_agent import extract_symptoms
from agents.medication_normalizer import normalize_medications

from agents.rag_agent import retrieve_medical_context

from agents.drug_agent import check_drug_interactions

from agents.risk_agent import predict_risk

from agents.soap_agent import generate_soap_note


class ClinicalService:

    def process(self, conversation):

        # -----------------------------
        # Symptom Extraction
        # -----------------------------

        patient = extract_symptoms(conversation)

        patient["medications"] = normalize_medications(
            patient["medications"]
        )

        # -----------------------------
        # RAG
        # -----------------------------

        symptoms = ", ".join(
            patient["symptoms"]
        )

        context = retrieve_medical_context(
            symptoms
        )

        # -----------------------------
        # Drug Interaction
        # -----------------------------

        drug_warnings = check_drug_interactions(
            patient["medications"]
        )

        # -----------------------------
        # Risk
        # -----------------------------

        risk = predict_risk(
            patient,
            context,
            drug_warnings
        )

        # -----------------------------
        # SOAP
        # -----------------------------

        soap = generate_soap_note(
            patient,
            context,
            drug_warnings
        )

        return {

            "patient_data": patient,

            "medical_context": context,

            "drug_warnings": drug_warnings,

            "risk_report": risk,

            "soap_note": soap

        }


clinical_service = ClinicalService()