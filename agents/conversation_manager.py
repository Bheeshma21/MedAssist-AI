from agents.memory_agent import patient_memory


class ConversationManager:

    def __init__(self):
        self.history = []

    def add_user_message(self, message):

        self.history.append({
            "role": "user",
            "content": message
        })

    def add_ai_message(self, message):

        self.history.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
        patient_memory.clear()


conversation_manager = ConversationManager()