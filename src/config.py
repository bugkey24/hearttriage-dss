"""Central configuration: criteria, weights, thresholds, and mappings.

All tunable DSS parameters live here — never hard-code them in modules.
"""

# --- Dataset -------------------------------------------------------------

COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "class",
    "subclass",
]

RAW_DATA_PATH = "data/raw/cleve.mod"
INTERIM_DATA_PATH = "data/interim/cleve_interim.csv"
PROCESSED_DATA_PATH = "data/processed/cleve_clean.csv"
TRIAGE_DATA_PATH = "data/processed/cleve_triage.csv"

# --- SAW Criteria ----------------------------------------------------------

CRITERIA = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca", "thal", "exang"]
BENEFIT = ["thalach"]
COST = ["age", "trestbps", "chol", "oldpeak", "ca", "thal", "exang"]

WEIGHTS = {
    "age": 0.10,
    "trestbps": 0.15,
    "chol": 0.10,
    "thalach": 0.15,
    "oldpeak": 0.15,
    "ca": 0.15,
    "thal": 0.10,
    "exang": 0.10,
}

# --- Triage Thresholds -----------------------------------------------------

THRESHOLDS = {
    "P1": 0.65,
    "P2": 0.45,
}

TRIAGE_LABELS = {
    "P1": "P1 - Emergency",
    "P2": "P2 - Urgent",
    "P3": "P3 - Non-Urgent",
}

TRIAGE_ACTIONS = {
    "P1": "Immediate treatment (< 5 minutes)",
    "P2": "Fast treatment (< 30 minutes)",
    "P3": "Can wait (< 60 minutes)",
}

# --- Categorical-to-Score Mappings -----------------------------------------

MAPPING = {
    "sex": {"male": 1, "fem": 0},
    "cp": {"angina": 1, "abnang": 2, "notang": 3, "asympt": 4},
    "fbs": {"true": 1, "fal": 0},
    "restecg": {"norm": 0, "abn": 1, "hyp": 2},
    "exang": {"true": 1, "fal": 0},
    "slope": {"up": 1, "flat": 2, "down": 3},
    # Dataset token is 'fix' (alias included for the canonical 'fixed' form)
    "thal": {"norm": 3, "fixed": 6, "fix": 6, "rev": 7},
}

NUMERIC_COLUMNS = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]
MISSING_MARKER = "?"
