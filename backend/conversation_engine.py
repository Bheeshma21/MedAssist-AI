from services.image_service import image_service
from services.language_service import language_service 
from backend.context_resolver import context_resolver
from agents.intent_agent import intent_agent
from memory.session_memory import session_memory

from services.qa_service import qa_service
from services.report_service import report_service
from services.clinical_service import clinical_service
from services.response_service import response_service

from database.database_service import database


class ConversationEngine:

    def __init__(self):

        self.history = []

    # =====================================================
    # Process Conversation
    # =====================================================

    def process(
        self,
        user_input,
        user_id,
        role="patient",
        session_id=None
    ):

        print("\n********** NEW CONVERSATION ENGINE **********")

        # ----------------------------------------
        # Create Chat Session
        # ----------------------------------------

        if session_id is None:

            session_id = database.create_chat_session(
                user_id=user_id,
                title=user_input[:40]
            )

        # ----------------------------------------
        # Save User Message
        # ----------------------------------------

        database.save_message(
            user_id=user_id,
            role="user",
            message=user_input,
            session_id=session_id
        )
        database.rename_if_new_chat(
            session_id,
            user_input[:40]
        )

        session_memory.add_message(
            "user",
            user_input
        )
                # ----------------------------------------
        # Language Preference
        # ----------------------------------------

        selected_language = language_service.detect_language_request(
            user_input
        )

        if selected_language:

            language_only_commands = [

                "telugu",
                "english",
                "hindi",
                "kannada",
                "tamil",
                "malayalam",

                "answer in telugu",
                "answer in english",
                "answer in hindi",
                "answer in kannada",
                "answer in tamil",
                "answer in malayalam",

                "reply in telugu",
                "reply in english",
                "reply in hindi",
                "reply in kannada",
                "reply in tamil",
                "reply in malayalam",

                "response in telugu",
                "response in english",
                "response in hindi",
                "response in kannada",
                "response in tamil",
                "response in malayalam",

                "respond in telugu",
                "respond in english",
                "respond in hindi",
                "respond in kannada",
                "respond in tamil",
                "respond in malayalam",

                "continue in telugu",
                "continue in english",
                "continue in hindi",
                "continue in kannada",
                "continue in tamil",
                "continue in malayalam",

                "switch to telugu",
                "switch to english",
                "switch to hindi",
                "switch to kannada",
                "switch to tamil",
                "switch to malayalam",

                "i want telugu",
                "i want english",
                "i want hindi",
                "i want kannada",
                "i want tamil",
                "i want malayalam"
            ]

            if user_input.strip().lower() in language_only_commands:

                response = (
                    f"✅ Language changed to {selected_language}.\n\n"
                    f"From now on I'll answer in {selected_language}."
                )

                database.save_message(
                    user_id=user_id,
                    role="assistant",
                    message=response,
                    session_id=session_id
                )

                session_memory.add_message(
                    "assistant",
                    response
                )

                return response, session_id

        # ----------------------------------------
        # Resolve Context & Intent
        # ----------------------------------------

        context = context_resolver.get_context()

        intent = intent_agent.classify(
            user_input
        )

        print("\n========== CONTEXT ==========")
        print(context)
        print("=============================\n")

        print(f"Detected Intent : {intent}")

        # ----------------------------------------
        # Route Request
        # ----------------------------------------

        try:

            # ====================================
            # IMAGE QUESTIONS
            # ====================================

            if context["has_image"] and intent == "image":

                image_result = image_service.analyze(
                    user_input
                )

                print("\n========== IMAGE RESULT ==========")
                print(image_result)
                print("==================================\n")

                response = image_result["analysis"]

            elif intent == "image":

                response = (
                    "ðŸ–¼ Please upload a medical image first so I can analyze it."
                )

            # ====================================
            # REPORT QUESTIONS
            # ====================================

            elif context["has_report"] and intent == "report":

                report_result = report_service.analyze(
                    user_input
                )

                print("\n========== REPORT RESULT ==========")
                print(report_result)
                print("===================================\n")

                response = report_result["analysis"]

            elif intent == "report":

                response = (
                    "ðŸ“„ Please upload a medical report first so I can answer questions about it."
                )

            # ====================================
            # GENERAL MEDICAL QUESTIONS
            # ====================================

            elif intent == "general":

                qa_result = qa_service.answer(
                    user_input
                )

                print("\n========== QA RESULT ==========")
                print(qa_result)
                print("================================\n")

                response = qa_result["answer"]

            # ====================================
            # SYMPTOM ANALYSIS
            # ====================================

            elif intent == "symptom":

                clinical_result = clinical_service.process(
                    user_input
                )

                print("\n========== CLINICAL RESULT ==========")
                print(clinical_result)
                print("=====================================\n")

                if role == "doctor":

                    response = response_service.doctor(
                        clinical_result
                    )

                else:

                    response = response_service.patient(
                        clinical_result
                    )

            # ====================================
            # MEDICATION
            # ====================================

            elif intent == "medication":
                qa_result = qa_service.answer(
                    user_input
                    )
                print("\n========== MEDICATION RESULT ==========")
                print(qa_result)
                print("=======================================\n")
                response = qa_result["answer"]
    

            # ====================================
            # UNKNOWN
            # ====================================

            else:

                response = (
                    "Sorry, I couldn't determine how to process your request."
                )

        except Exception:

            import traceback

            print("\n========== ENGINE ERROR ==========")
            traceback.print_exc()

            response = (
                "Sorry, an internal error occurred while processing your request."
            )

        # ----------------------------------------
        # Print Final Response
        # ----------------------------------------

        print("\n========== FINAL RESPONSE ==========")
        print(response)
        print("====================================\n")

        # ----------------------------------------
        # Save Assistant Response
        # ----------------------------------------

        database.save_message(
            user_id=user_id,
            role="assistant",
            message=response,
            session_id=session_id
        )

        session_memory.add_message(
            "assistant",
            response
        )

        self.history.append({
            "role": "user",
            "content": user_input
        })

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response, session_id

    # =====================================================
    # Load Chat History
    # =====================================================

    def load_history(
        self,
        user_id,
        session_id
    ):

        rows = database.get_chat_history(
            user_id,
            session_id
        )

        self.history = []

        for row in rows:

            self.history.append({

                "role": row["role"],

                "content": row["message"]

            })

        return self.history

    # =====================================================
    # Get All Chat Sessions
    # =====================================================

    def get_sessions(
        self,
        user_id
    ):

        return database.get_chat_sessions(
            user_id
        )

    # =====================================================
    # Clear Memory
    # =====================================================

    def clear(self):

        self.history = []

    # =====================================================
    # Get Current History
    # =====================================================

    def get_history(self):

        return self.history


conversation_engine = ConversationEngine()