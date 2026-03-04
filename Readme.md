# ZenTrades AI - Clara Answers Automation Pipeline

## Overview

This project demonstrates a **zero-cost automation pipeline** for Clara Answers, an AI-powered voice agent.  
The pipeline converts demo call transcripts into a preliminary Retell agent (v1) and updates it with onboarding call data (v2).

It simulates Clara's real-world workflow: **human conversation → structured rules → AI agent configuration → production-ready prompt**.

---

## Project Structure

```
/Zentrade
│
├─ /dataset
│   ├─ /demo                    # Demo call transcripts
│   │   ├─ transcript.txt        # Original demo (ben001)
│   │   ├─ demo2.txt            # Mike's Plumbing
│   │   ├─ demo3.txt            # GreenLeaf Medical
│   │   ├─ demo4.txt            # TechPro Solutions
│   │   └─ demo5.txt            # Santos Property
│   └─ /onboarding              # Onboarding call transcripts
│       ├─ onboard1.txt
│       ├─ onboard2.txt
│       ├─ onboard3.txt
│       ├─ onboard4.txt
│       └─ onboard5.txt
│
├─ /scripts
│   ├─ batch_process.py         # Batch processes all transcripts
│   ├─ dashboard.py             # HTML dashboard generator
│   ├─ diff_viewer.py           # v1 vs v2 diff viewer
│   ├─ simulate_call_v2_import.py  # Simulates agent calls
│   ├─ test_agent_v2.py         # Tests agent configuration
│   └─ ... (other utilities)
│
├─ /workflows
│   ├─ clara_answers_pipeline.json  # n8n workflow export
│   └─ SETUP.md                 # n8n setup guide
│
├─ /outputs
│   ├─ dashboard.html           # Generated HTML dashboard
│   ├─ tasks.json               # Task tracker
│   └─ /accounts/<account_id>
│       ├─ /v1
│       │   ├─ account_memo.json
│       │   └─ retell_agent_spec.json
│       ├─ /v2
│       │   ├─ account_memo.json
│       │   ├─ retell_agent_spec.json
│       │   └─ changelog_v2.json
│       └─ /changelog
│           └─ changes.json
│
├─ docker-compose.yml           # n8n Docker setup
└─ README.md
```

---

## Architecture

### Pipeline Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Demo Call      │────▶│  Extract Info   │────▶│  Generate v1    │
│  Transcript     │     │  (Rule-based)   │     │  Agent Spec     │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                            │
                                                            ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Onboarding     │────▶│  Update Info     │────▶│  Generate v2    │
│  Transcript     │     │  (Merge)         │     │  Agent Spec     │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                            │
                                                            ▼
                                                 ┌─────────────────┐
                                                 │  Changelog      │
                                                 │  (v1 → v2)      │
                                                 └─────────────────┘
```

### Data Flow

1. **Input**: Transcript files (demo or onboarding calls)
2. **Processing**: Rule-based extraction of business hours, services, emergencies
3. **Output**: 
   - Account Memo JSON (structured account data)
   - Retell Agent Spec JSON (AI agent configuration)
   - Changelog JSON (version changes)
   - Task tracker item

---

## Features

- ✅ **Zero-cost**, fully reproducible workflow
- ✅ **Batch processing** for multiple accounts (5 demo + 5 onboarding)
- ✅ **Versioned** agent specs (v1 → v2) with changelog
- ✅ **Rule-based extraction** (no paid LLM required)
- ✅ **n8n workflow** for orchestration (optional)
- ✅ **Docker support** for easy deployment
- ✅ **Task tracker** (outputs/tasks.json)
- ✅ **Simple Dashboard** (outputs/dashboard.html)
- ✅ **Diff Viewer** (scripts/diff_viewer.py)
- ✅ Handles missing or unknown information responsibly
- ✅ Clear separation of demo-derived and onboarding-confirmed rules

---

## Scripts

| Script | Purpose |
|--------|---------|
| `batch_process.py` | Process all demo + onboarding transcripts |
| `dashboard.py` | Generate HTML dashboard |
| `diff_viewer.py` | Show v1 vs v2 differences |
| `simulate_call_v2_import.py` | Simulate agent handling a call |
| `test_agent_v2.py` | Test agent configuration |

---

## How to Run

### Option 1: Quick Start (Python Scripts)

1. **Clone the repository**
2. **Run batch processing:**

```bash
python scripts/batch_process.py
```

3. **View dashboard:**

```bash
python scripts/dashboard.py
```

4. **View diff for an account:**

```bash
python scripts/diff_viewer.py ben001
```

5. **Simulate a call:**

```bash
python scripts/simulate_call_v2_import.py
```

### Option 2: Using n8n (Docker)

1. **Start n8n:**

```bash
docker-compose up -d
```

2. **Access n8n UI:** http://localhost:5678
   - Username: `admin`
   - Password: `clara123`

3. **Import workflow:**
   - Go to Workflows → Import from File
   - Select `workflows/clara_answers_pipeline.json`

4. **Activate** the workflow

See `workflows/SETUP.md` for detailed instructions.

---

## Dataset

### Demo Calls (5 files)
| File | Account ID | Company |
|------|------------|---------|
| transcript.txt | ben001 | Ben's Electric Solutions |
| demo2.txt | plum001 | Mike's Plumbing Services |
| demo3.txt | med001 | GreenLeaf Medical Clinic |
| demo4.txt | tech001 | TechPro Solutions LLC |
| demo5.txt | prop001 | Santos Property Management |

### Onboarding Calls (5 files)
| File | Account ID |
|------|------------|
| onboard1.txt | ben001 |
| onboard2.txt | plum001 |
| onboard3.txt | med001 |
| onboard4.txt | tech001 |
| onboard5.txt | prop001 |

---

## Output Format

### Account Memo JSON
```json
{
  "account_id": "ben001",
  "company_name": "Ben's Electric Solutions",
  "business_hours": {
    "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "start": "09:00",
    "end": "18:00",
    "timezone": "EST"
  },
  "services_supported": ["Electrical Maintenance", "Emergency Repairs"],
  "emergency_definition": ["Power Outage", "Fire Alarm"],
  "emergency_routing_rules": ["Call 24/7 hotline", "Notify onsite manager"],
  "call_transfer_rules": { "timeouts": "30s", "retries": 2, "fallback": "Voicemail" },
  ...
}
```

### Retell Agent Spec JSON
```json
{
  "agent_name": "BenElectricAgent",
  "voice_style": "basic",
  "system_prompt": "You are an automated assistant...",
  "key_variables": { ... },
  "call_transfer_protocol": { ... },
  "version": "v1"
}
```

### Changelog JSON
```json
{
  "account_id": "ben001",
  "version_from": "v1",
  "version_to": "v2",
  "changes": [
    { "field": "services_supported", "old_value": [...], "new_value": [...] }
  ]
}
```

### Task Tracker JSON
```json
{
  "tasks": [
    { "id": "task_ben001_demo_v1", "account_id": "ben001", "type": "demo_v1", "status": "completed" }
  ],
  "summary": { "total": 10, "completed": 10, "pending": 0 }
}
```

---

## Known Limitations

1. **Rule-based extraction**: Uses simple keyword matching; may miss nuanced information
2. **No real Retell API integration**: Outputs are spec files, not live agent deployments
3. **No speech-to-text**: Requires pre-transcribed text input
4. **No external LLM**: Uses template-based prompt generation (zero-cost constraint)
5. **Limited error handling**: Basic validation only
6. **Single timezone**: Defaults to PST/EST; needs configuration for other zones

---

## Future Improvements

- [ ] Add local LLM (Ollama) for better extraction
- [ ] Real Retell API integration (requires paid account)
- [ ] Speech-to-text integration (Whisper)
- [ ] Dashboard for visualizing call handling
- [ ] Diff viewer for v1 vs v2 comparison
- [ ] Asana/task integration for tracking
- [ ] Email notifications for new accounts

---

## Demo Video

> [Loom Video Link: YOUR_LINK_HERE]

---

## Credits

ZenTrades AI - Clara Answers Intern Project  
Batch: 2026  
Author: Suneeth S

---

## Contact

For questions or issues, please review the workflow setup guide in `/workflows/SETUP.md`.

