from memory.session_memory import session_memory


class IntentAgent:

    def _match_keywords(self, message: str, keywords: list[str]) -> bool:
        """
        Match single-word keywords as whole words.
        Match multi-word keywords as phrases.
        """
        words = set(message.split())

        for keyword in keywords:

            keyword = keyword.lower()

            # Phrase (e.g. "ct scan", "side effect")
            if " " in keyword:
                if keyword in message:
                    return True

            # Single word
            else:
                if keyword in words:
                    return True

        return False

    def classify(self, message: str) -> str:

        message = message.lower().strip()

        # ---------------------------------------------
        # Uploaded Resources
        # ---------------------------------------------

        report_in_memory = (
            session_memory.get_report_text() is not None
        )

        image_in_memory = (
            session_memory.get_image() is not None
        )

        # ---------------------------------------------
        # Image Follow-up
        # ---------------------------------------------

        image_followup_keywords = [

            "image",
            "picture",
            "photo",
            "xray",
            "x-ray",
            "mri",
            "ct scan",
            "scan",
            "ecg",
            "fracture",
            "bone",
            "lung",
            "brain",
            "heart",
            "skin",
            "rash",
            "lesion",
            "tumor",
            "eye",
            "retina",
            "wound",
            "ultrasound",
            "visible",
            "abnormality",
            "abnormal",
            "normal",
            "findings",
            "what do you see",
            "what is visible",
            "explain this image",
            "explain this xray",
            "is there a fracture",
            "is anything wrong",
            "can you analyze this",
            "analyze this image",
            "analyze this xray"

        ]

        if image_in_memory:

            if self._match_keywords(
                message,
                image_followup_keywords
            ):
                return "image"

        # ---------------------------------------------
        # Report Follow-up
        # ---------------------------------------------

        report_followup_keywords = [

            "report",
            "result",
            "results",
            "value",
            "level",
            "normal",
            "abnormal",
            "high",
            "low",
            "hemoglobin",
            "hb",
            "hgb",
            "rbc",
            "wbc",
            "platelet",
            "hematocrit",
            "mcv",
            "mch",
            "mchc",
            "rdw",
            "blood count",
            "cbc",
            "should i worry",
            "is it dangerous",
            "can i exercise",
            "what should i eat",
            "diet",
            "food",
            "treatment",
            "medicine",
            "supplements",
            "summarize my report",
            "explain my report",
            "interpret my report"

        ]

        if report_in_memory:

            if self._match_keywords(
                message,
                report_followup_keywords
            ):
                return "report"

        # ---------------------------------------------
        # Image Queries
        # ---------------------------------------------

        image_keywords = [

            "image",
            "picture",
            "photo",
            "xray",
            "x-ray",
            "mri",
            "ct scan",
            "scan",
            "ecg",
            "fracture",
            "bone",
            "lung",
            "brain",
            "heart",
            "skin",
            "rash",
            "lesion",
            "tumor",
            "eye",
            "retina",
            "ultrasound",
            "wound"

        ]

        if self._match_keywords(
            message,
            image_keywords
        ):
            return "image"

        # ---------------------------------------------
        # Report Queries
        # ---------------------------------------------

        report_keywords = [

            "report",
            "blood report",
            "blood test",
            "lab report",
            "cbc",
            "prescription"

        ]

        if self._match_keywords(
            message,
            report_keywords
        ):
            return "report"

        # ---------------------------------------------
        # Medication
        # ---------------------------------------------

        medication_keywords = [

            "medicine",
            "tablet",
            "drug",
            "dose",
            "dosage",
            "prescribe",
            "paracetamol",
            "ibuprofen",
            "antibiotic",
            "side effect",
            "side effects",
            "uses",
            "interaction"

        ]

        if self._match_keywords(
            message,
            medication_keywords
        ):
            return "medication"

        # ---------------------------------------------
        # Symptoms
        # ---------------------------------------------

        symptom_keywords = [

            "pain",
            "fever",
            "cough",
            "headache",
            "vomiting",
            "nausea",
            "dizziness",
            "cold",
            "breathing",
            "chest pain",
            "fatigue",
            "weakness",
            "suffering",
            "having"

        ]

        if self._match_keywords(
            message,
            symptom_keywords
        ):
            return "symptom"

        # ---------------------------------------------
        # General
        # ---------------------------------------------

        return "general"


intent_agent = IntentAgent()