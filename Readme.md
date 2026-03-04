
# ZenTrades AI - Clara Answers Automation Pipeline

## Overview
This project demonstrates a zero-cost automation pipeline for Clara Answers, an AI-powered voice agent.  
The pipeline converts demo call transcripts into a preliminary Retell agent (v1) and updates it with onboarding call data (v2).  

It simulates Clara’s real-world workflow: **human conversation → structured rules → AI agent configuration → production-ready prompt**.

---

## Project Structure
```

/Zentrade
│
├─ /scripts
│   └─ simulate_call_v2_import.py   # Script to simulate agent handling calls
│
├─ /outputs/accounts/<account_id>
│   ├─ /v1
│   │   ├─ account_memo.json
│   │   └─ retell_agent_spec.json
│   ├─ /v2
│   │   ├─ account_memo_updated.json
│   │   ├─ changelog_v2.json
│   │   ├─ retail_agent_spec_v2.json
│   │   └─ retail_agent_import_v2.json
│
└─ README.md

````

---

## Pipeline Workflow

### Step 1: v1 Agent Generation (Demo Call)
- Input: Demo call transcript
- Extract key information into **account memo JSON**
- Generate preliminary **Retell agent spec (v1)**:
  - Business hours
  - Emergency definitions
  - Call routing rules
  - Transfer and fallback protocols
- Output stored in `/v1` folder

### Step 2: v2 Agent Update (Onboarding Call)
- Input: Onboarding call transcript or structured form
- Update account memo and agent spec with confirmed rules
- Preserve **version history**
- Create a **changelog** for all updates
- Output stored in `/v2` folder

### Step 3: Simulate Call
- Run `simulate_call_v2_import.py` to simulate agent handling:
  - Business hours vs after-hours routing
  - Emergency vs non-emergency calls
  - Automatic use of account memo and agent spec v1 or v2
- Console outputs **call summary**

---

## Features
- Zero-cost, fully reproducible workflow
- Versioned agent specs (v1 → v2) with changelog
- Handles missing or unknown information responsibly
- Clear separation of demo-derived assumptions and onboarding-confirmed rules
- Repeatable, batch-capable, idempotent pipeline

---

## How to Run

1. Clone the repository
2. Place demo and onboarding transcripts under `/outputs/accounts/<account_id>/`
3. Run the simulation:

```bash
python scripts/simulate_call_v2_import.py
````

4. Check `/v1` and `/v2` folders for:

   * Account memo JSON
   * Retell agent spec JSON
   * Changelog (for v2)

---

## Future Improvements

* Batch processing for multiple accounts
* n8n integration for workflow orchestration
* Dashboard to visualize call handling and version diffs
* Local speech-to-text support for raw audio input

---

## Notes

* Zero-cost project; no paid APIs are used
* Only structured transcripts are input
* For educational/demo purposes; real deployment requires Retell account integration

---
## Demo Video
Watch the workflow in action: [Loom Video Link](YOUR_LINK_HERE)


## Contact

ZenTrades AI - Clara Answers Intern Project
Batch: 2026
Author: Suneeth S

```

---

