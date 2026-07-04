class ResponseService:

    def patient(self, clinical_result):

        risk = clinical_result["risk_report"]

        return f"""
# 🩺 Clinical Assessment

## Possible Conditions

{', '.join(risk["possible_conditions"]) or "No significant condition detected"}

---

## Risk Level

{risk["risk_level"]}

---

## Recommended Action

{risk["recommended_action"]}

---

This assessment is AI generated.

Please consult a healthcare professional for diagnosis and treatment.
"""

    def doctor(self, clinical_result):

        patient = clinical_result["patient_data"]
        risk = clinical_result["risk_report"]
        drug = clinical_result["drug_warnings"]
        soap = clinical_result["soap_note"]

        return f"""
# 🩺 Clinical Decision Support

## Patient Summary

**Symptoms:**
{', '.join(patient.get("symptoms", [])) or "Not Available"}

**Duration:**
{patient.get("duration", "Not Available")}

**Medications:**
{', '.join(patient.get("medications", [])) or "None"}

**Allergies:**
{', '.join(patient.get("allergies", [])) or "None"}

---

## Differential Diagnosis

{', '.join(risk.get("possible_conditions", [])) or "No significant condition detected"}

---

## Risk Assessment

{risk.get("risk_level", "Unknown")}

---

## Recommended Clinical Action

{risk.get("recommended_action", "Not Available")}

---

## Drug Interaction Assessment

{drug if drug else "No clinically significant interactions detected."}

---

## SOAP Note

{soap}

---

This output is AI-assisted clinical decision support.

Clinical judgment should always take precedence.
"""

    def guest(self, clinical_result):

        return self.patient(clinical_result)


response_service = ResponseService()