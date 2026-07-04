from memory.session_memory import session_memory


class ContextResolver:

    def get_context(self):

        return {

            "has_report":
                session_memory.get_report() is not None,

            "report_path":
                session_memory.get_report(),

            "report_text":
                session_memory.get_report_text(),

            "has_image":
                session_memory.get_image() is not None,

            "image_path":
                session_memory.get_image(),

            "conversation":
                session_memory.get_conversation()

        }


context_resolver = ContextResolver()