import os
from gtts import gTTS
from langdetect import detect


class VoiceService:

    def generate_audio(self, text):

        os.makedirs(
            "data/audio",
            exist_ok=True
        )

        output_path = "data/audio/response.mp3"

        try:

            detected = detect(text)

        except Exception:

            detected = "en"

        language_map = {

            "en": "en",
            "hi": "hi",
            "te": "te",
            "kn": "kn",
            "ta": "ta",
            "ml": "ml"

        }

        tts_language = language_map.get(
            detected,
            "en"
        )

        tts = gTTS(

            text=text,

            lang=tts_language,

            slow=False

        )

        tts.save(output_path)

        return output_path


voice_service = VoiceService()