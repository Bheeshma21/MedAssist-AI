import pyperclip


class ShareService:

    def copy(self, text):

        try:

            pyperclip.copy(text)

            return True

        except:

            return False


share_service = ShareService()