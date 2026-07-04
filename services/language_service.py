import re
import streamlit as st


class LanguageService:

    def __init__(self):

        if "preferred_language" not in st.session_state:
            st.session_state.preferred_language = "English"

    def detect_language_request(self, message: str):

        message = message.lower().strip()

        language_patterns = {

            "English": [

                r"english",
                r"answer in english",
                r"reply in english",
                r"respond in english",
                r"response in english",
                r"continue in english",
                r"switch to english",
                r"english please",
                r"i want english"

            ],

            "Hindi": [

                r"hindi",
                r"answer in hindi",
                r"reply in hindi",
                r"respond in hindi",
                r"response in hindi",
                r"continue in hindi",
                r"switch to hindi",
                r"i want hindi",
                r"hindi me",
                r"hindi mein"

            ],

            "Telugu": [

                r"telugu",
                r"answer in telugu",
                r"reply in telugu",
                r"respond in telugu",
                r"response in telugu",
                r"continue in telugu",
                r"switch to telugu",
                r"i want telugu",
                r"i want answer in telugu",
                r"telugu lo",
                r"telugulo",
                r"telugu lo cheppu",
                r"telugu lo explain"

            ],

            "Kannada": [

                r"kannada",
                r"answer in kannada",
                r"reply in kannada",
                r"respond in kannada",
                r"response in kannada",
                r"continue in kannada",
                r"switch to kannada",
                r"i want kannada",
                r"kannada dalli"

            ],

            "Tamil": [

                r"tamil",
                r"answer in tamil",
                r"reply in tamil",
                r"respond in tamil",
                r"response in tamil",
                r"continue in tamil",
                r"switch to tamil",
                r"i want tamil"

            ],

            "Malayalam": [

                r"malayalam",
                r"answer in malayalam",
                r"reply in malayalam",
                r"respond in malayalam",
                r"response in malayalam",
                r"continue in malayalam",
                r"switch to malayalam",
                r"i want malayalam"

            ]

        }

        for language, patterns in language_patterns.items():

            for pattern in patterns:

                if re.search(pattern, message):

                    st.session_state.preferred_language = language

                    return language

        return None

    def get_language(self):

        return st.session_state.get(
            "preferred_language",
            "English"
        )

    def language_instruction(self):

        language = self.get_language()

        if language == "English":

            return """
IMPORTANT:

Answer ONLY in English.

Use simple patient-friendly language.
"""

        return f"""
IMPORTANT:

Answer ONLY in natural conversational {language}.

Do NOT translate every medical term.

Keep these terms in English:

Hemoglobin
Blood Pressure
Diabetes
Cholesterol
CBC
ECG
MRI
CT Scan
Iron
Vitamin D
Vitamin B12
Platelets
RBC
WBC
Kidney
Liver
HbA1c

Explain everything else naturally in {language}.

Use the way Indian doctors normally speak.

Never say that you cannot answer in {language}.
"""


language_service = LanguageService()