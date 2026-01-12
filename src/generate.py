import os
import csv
import random
from faker import Faker

fake = Faker()

# ---------------- CONFIG ----------------
NUM_MOLECULES = 5000
REPORTS_PER_MOLECULE = 2
EXPERIMENTS_PER_MOLECULE = 4

BASE_DIR = "data"
REPORT_DIR = f"{BASE_DIR}/raw/reports"
EXP_DIR = f"{BASE_DIR}/raw/experiments"
META_DIR = f"{BASE_DIR}/metadata"
TRAIN_DIR = f"{BASE_DIR}/training"

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(EXP_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)
os.makedirs(TRAIN_DIR, exist_ok=True)

THERAPEUTIC_AREAS = ["Oncology", "Cardiology", "Neurology", "Immunology"]
SYNTHESIS_METHODS = [
    "multi-step organic synthesis",
    "esterification followed by purification",
    "aromatic substitution reaction",
    "catalytic hydrogenation"
]

# ---------------- STEP 1: MOLECULE METADATA ----------------
molecules = []

for i in range(NUM_MOLECULES):
    mol_id = f"MOL{i:05d}"
    molecules.append({
        "molecule_id": mol_id,
        "therapeutic_area": random.choice(THERAPEUTIC_AREAS),
        "molecular_weight": round(random.uniform(250, 550), 2),
        "logP": round(random.uniform(1.0, 5.0), 2),
        "hbond_donors": random.randint(0, 5),
        "hbond_acceptors": random.randint(1, 10)
    })

with open(f"{META_DIR}/molecules.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=molecules[0].keys()
    )
    writer.writeheader()
    writer.writerows(molecules)

print("✅ Molecule metadata generated")

# ---------------- STEP 2: INTERNAL RESEARCH REPORTS ----------------
for mol in molecules:
    for r in range(REPORTS_PER_MOLECULE):
        report_text = f"""
Molecule ID: {mol['molecule_id']}
Therapeutic Area: {mol['therapeutic_area']}

Synthesis Summary:
The molecule was synthesized using {random.choice(SYNTHESIS_METHODS)}.

LCMS Results:
Observed m/z peak at {mol['molecular_weight']} corresponding to expected molecular weight.

NMR Summary:
Proton NMR confirmed characteristic peaks between 7.0–8.0 ppm.

Conclusion:
The molecule meets internal analytical validation criteria and is suitable for further evaluation.
"""
        with open(
            f"{REPORT_DIR}/{mol['molecule_id']}_report_{r}.txt", "w"
        ) as f:
            f.write(report_text)

print("✅ Research reports generated")

# ---------------- STEP 3: EXPERIMENT FILES ----------------
EXPERIMENT_TYPES = ["LCMS", "NMR", "HPLC"]

for mol in molecules:
    for e in range(EXPERIMENTS_PER_MOLECULE):
        exp_type = random.choice(EXPERIMENT_TYPES)
        exp_text = f"""
Experiment Type: {exp_type}
Molecule ID: {mol['molecule_id']}
Result: PASS
Details: {fake.sentence()}
"""
        with open(
            f"{EXP_DIR}/{exp_type}_{mol['molecule_id']}_{e}.txt", "w"
        ) as f:
            f.write(exp_text)

print("✅ Experiment files generated")

# ---------------- STEP 4: ML TRAINING DATA ----------------
INTENTS = ["similarity", "experiment", "summary"]

with open(f"{TRAIN_DIR}/intent_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["query", "intent"])
    for mol in molecules[:1000]:
        writer.writerow([f"Find similar molecules to {mol['molecule_id']}", "similarity"])
        writer.writerow([f"Show LCMS results for {mol['molecule_id']}", "experiment"])
        writer.writerow([f"Summarize research on {mol['molecule_id']}", "summary"])

with open(f"{TRAIN_DIR}/reranker_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["query", "doc_id", "relevant"])
    for mol in molecules[:500]:
        writer.writerow([f"LCMS results for {mol['molecule_id']}", f"LCMS_{mol['molecule_id']}", 1])
        writer.writerow([f"LCMS results for {mol['molecule_id']}", f"HPLC_{mol['molecule_id']}", 0])

print("✅ ML training data generated")

print("\n🎉 DATA GENERATION COMPLETE")
print("Molecules:", NUM_MOLECULES)
print("Reports:", NUM_MOLECULES * REPORTS_PER_MOLECULE)
print("Experiments:", NUM_MOLECULES * EXPERIMENTS_PER_MOLECULE)
