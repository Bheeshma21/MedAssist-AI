def check_drug_interactions(medications):
    interactions = {
        ("warfarin", "aspirin"): {
            "severity": "High",
            "warning": "Increased bleeding risk"
        },

        ("warfarin", "ibuprofen"): {
            "severity": "High",
            "warning": "Risk of severe bleeding"
        },

        ("warfarin", "clopidogrel"): {
            "severity": "High",
            "warning": "Very high bleeding risk"
        },

        ("aspirin", "clopidogrel"): {
            "severity": "Moderate",
            "warning": "Increased bleeding risk"
        },

        ("ramipril", "ibuprofen"): {
            "severity": "Moderate",
            "warning": "Reduced antihypertensive effect and kidney injury risk"
        },

        ("furosemide", "ibuprofen"): {
            "severity": "Moderate",
            "warning": "Reduced diuretic effect"
        },

        ("simvastatin", "clarithromycin"): {
            "severity": "High",
            "warning": "Risk of severe muscle injury (Rhabdomyolysis)"
        },

        ("metformin", "contrast dye"): {
            "severity": "High",
            "warning": "Risk of lactic acidosis"
        },

        ("digoxin", "furosemide"): {
            "severity": "Moderate",
            "warning": "Electrolyte imbalance may increase digoxin toxicity"
        },

        ("losartan", "potassium"): {
            "severity": "Moderate",
            "warning": "Risk of hyperkalemia"
        }
    }

    found = []

    meds = [m.lower() for m in medications]

    for (drug1, drug2), info in interactions.items():

        if drug1 in meds and drug2 in meds:

            found.append({
                "drug1": drug1.title(),
                "drug2": drug2.title(),
                "severity": info["severity"],
                "warning": info["warning"]
            })

    return found