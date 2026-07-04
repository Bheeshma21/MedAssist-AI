class ConversationMemory:

    def __init__(self):

        self.sessions = {}

    def add(self, session_id, role, message):

        if session_id not in self.sessions:

            self.sessions[session_id] = []

        self.sessions[session_id].append({

            "role": role,

            "content": message

        })

    def history(self, session_id):

        return self.sessions.get(session_id, [])

    def clear(self, session_id):

        self.sessions[session_id] = []


conversation_memory = ConversationMemory()