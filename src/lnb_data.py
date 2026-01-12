import os
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -------- CONFIG --------
NUM_LNB_ENTRIES = 4000
LNB_DIR = "data/raw/lab_notebooks"

os.makedirs(LNB_DIR, exist_ok=True)

SCIENTISTS = [
    "Researcher_A",
    "Researcher_B",
    "Researcher_C",
    "Senior_Scientist_1",
    "PostDoc_2"
]

OBJECTIVES = [
    "Explore alternate synthesis route",
    "Test solvent impact on yield",
    "Validate preliminary reaction conditions",
    "Investigate impurity formation",
    "Assess reaction temperature sensitivity"
]

OBSERVATIONS = [
    "Reaction yield was lower than expected.",
    "Unexpected impurity detected during LCMS run.",
    "Reaction completed faster than anticipated.",
    "Product showed partial degradation.",
    "Purity levels varied across batches."
]

NOTES = [
    "May require solvent optimization.",
    "Temperature control could improve results.",
    "Repeat experiment with modified conditions.",
    "Consult analytical team for deeper review.",
    "Result inconclusive, needs repetition."
]

START_DATE = datetime(2023, 1, 1)

# -------- GENERATE LNB FILES --------
for i in range(NUM_LNB_ENTRIES):
    notebook_id = f"LNB_{2024}_{i:05d}"
    scientist = random.choice(SCIENTISTS)
    molecule_id = f"MOL{random.randint(0,4999):05d}"
    date = START_DATE + timedelta(days=random.randint(0, 500))

    content = f"""
Notebook ID: {notebook_id}
Scientist: {scientist}
Date: {date.strftime('%Y-%m-%d')}
Molecule ID: {molecule_id}

Objective:
{random.choice(OBJECTIVES)} for {molecule_id}.

Observations:
{random.choice(OBSERVATIONS)}

Notes:
{random.choice(NOTES)}

Status:
Exploratory – not validated.
"""

    file_path = os.path.join(LNB_DIR, f"{notebook_id}.txt")
    with open(file_path, "w") as f:
        f.write(content.strip())

print(f"✅ Generated {NUM_LNB_ENTRIES} Lab Notebook entries")
