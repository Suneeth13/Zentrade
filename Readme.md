# Clara Answers – Zentrade Agent Automation

## Overview
This project automates creation and updating of a retail voice agent.

Workflow:
1. Demo call → Generates v1 Account Memo + Agent Spec
2. Onboarding call → Updates to v2
3. Generates changelog
4. Simulates call handling

All scripts run locally with zero paid tools.

---

## How to Run

### Step 1: Generate v1 Agent
python scripts/init_agent_v2.py

### Step 2: Process Call + Create v2
python scripts/process_calls_v2.py

### Step 3: Prepare Import JSON
python scripts/prepare_agent_v2_import.py

### Step 4: Test Import
python scripts/test_import_v2.py

### Step 5: Simulate Call
python scripts/simulate_call_v2_import.py

---

## Outputs Location

outputs/accounts/ben001/v1/
outputs/accounts/ben001/v2/

Files Generated:
- account_memo.json
- retail_agent_spec_v2.json
- changelog_v2.json
- retail_agent_v2_import.json

---

## Notes
- Currently supports 1 demo + 1 onboarding call
- Can be extended for batch processing
- No paid APIs used