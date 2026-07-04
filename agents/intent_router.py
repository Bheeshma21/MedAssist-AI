from enum import Enum


class Intent(Enum):
    CONSULTATION = "consultation"
    QUESTION = "question"
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"
    VOICE = "voice"
    DRUG = "drug"


def detect_intent(user_input="", file_type=None):

    text = user_input.lower()

    if file_type == "pdf":
        return Intent.DOCUMENT

    if file_type in ["png", "jpg", "jpeg"]:
        return Intent.IMAGE

    if file_type in ["mp4", "avi", "mov"]:
        return Intent.VIDEO

    if file_type in ["wav", "mp3", "m4a"]:
        return Intent.VOICE

    drug_keywords = [
        "medicine",
        "tablet",
        "drug",
        "interaction",
        "dose",
        "paracetamol",
        "ibuprofen"
    ]

    if any(word in text for word in drug_keywords):
        return Intent.DRUG

    consultation_keywords = [
        "pain",
        "fever",
        "cough",
        "breath",
        "swelling",
        "vomiting",
        "headache",
        "dizziness"
    ]

    if any(word in text for word in consultation_keywords):
        return Intent.CONSULTATION

    return Intent.QUESTION