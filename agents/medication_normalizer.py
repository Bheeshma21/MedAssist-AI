from difflib import get_close_matches

KNOWN_MEDICATIONS = [
    "Aspirin",
    "Warfarin",
    "Ramipril",
    "Simvastatin",
    "Metformin",
    "Insulin",
    "Atorvastatin",
    "Clopidogrel",
    "Losartan",
    "Amlodipine",
    "Bisoprolol",
    "Furosemide",
]

# Common Whisper spelling mistakes / aliases
ALIASES = {
    "ramiprol": "Ramipril",
    "semestan": "Simvastatin",
    "simvastin": "Simvastatin",
    "atorvastin": "Atorvastatin",
    "metforman": "Metformin",
    "lasix": "Furosemide",
    "asa": "Aspirin",
}


def normalize_medications(medications):

    normalized = []

    for med in medications:

        med_clean = med.strip()

        # First check known aliases
        alias = ALIASES.get(med_clean.lower())

        if alias:
            normalized.append(alias)
            continue

        # Then use fuzzy matching
        match = get_close_matches(
            med_clean,
            KNOWN_MEDICATIONS,
            n=1,
            cutoff=0.6
        )

        if match:
            normalized.append(match[0])
        else:
            normalized.append(med_clean)

    return normalized