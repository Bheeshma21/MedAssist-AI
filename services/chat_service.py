from database.database_service import database


class ChatService:

    def load_history(
        self,
        user_id,
        session_id
    ):

        return database.get_chat_history(
            user_id,
            session_id
        )

    def save(
        self,
        user_id,
        role,
        message,
        session_id
    ):

        database.save_message(
            user_id,
            role,
            message,
            session_id
        )


chat_service = ChatService()