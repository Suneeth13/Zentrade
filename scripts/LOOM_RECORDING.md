
# Loom Video Recording Script - Complete Guide

This document provides a step-by-step guide for creating your 3-5 minute Loom video demonstrating the Clara Answers Automation Pipeline.

---

## Latest Update: Fireflies Integration

The pipeline now supports importing demo call recordings directly from Fireflies.ai. The demo call recording from:
- **URL**: https://app.fireflies.ai/view/01KEFDQJ7E0EZR9WDFBWK774D9
- **Transcript**: `dataset/onboarding/onboard.txt` (full Fireflies transcript)
- **Parsed Info**: `dataset/onboarding/onboard1.txt` (structured extracted data)

This demo call with Ben (Ben's Electric Solutions) has been processed through the pipeline, generating complete v1 and v2 agent configurations.

---

## Pre-Recording Checklist

Before you start recording, ensure you have:

- [ ] Terminal/Command Prompt open
- [ ] Navigated to project directory: `cd d:/Zentrade`
- [ ] Loom extension installed in browser
- [ ] Screen recording ready

---

## Video Structure (Recommended)

| Time | Section | Duration |
|------|---------|----------|
| 0:00-0:30 | Introduction | 30 sec |
| 0:30-1:30 | Batch Processing Demo | 1 min |
| 1:30-2:00 | Dashboard Overview | 30 sec |
| 2:00-2:30 | Diff Viewer Demo | 30 sec |
| 2:30-3:30 | File Outputs | 1 min |
| 3:30-4:00 | Agent Simulation | 30 sec |
| 4:00-4:30 | Closing | 30 sec |

---

## Detailed Recording Steps

### SECTION 1: Introduction (0:00 - 0:30)

**Action:** Show your screen and introduce yourself.

**Say:** "Hi, I'm [Your Name]. Today I'll demonstrate the Clara Answers Automation Pipeline - a zero-cost workflow that converts demo call transcripts into AI agent configurations."

**Action:** Show project structure in terminal:

```bash
dir /b
```

Or list files in VS Code Explorer.

**Say:** "Here's our project structure with datasets, scripts, workflows, and outputs."

---

### SECTION 2: Batch Processing (0:30 - 1:30)

**Action:** Run the batch processor:

```bash
python scripts/batch_process.py
```

**What to show:**
- The terminal output showing all 5 demo calls processed
- The terminal output showing all 5 onboarding calls processed
- Point out the "Tasks created: 10, Completed: 10" message

**Say:** "This is the main batch processing script. It reads all 10 transcript files - 5 demo calls and 5 onboarding calls. For each demo call, it generates a v1 agent configuration. For each onboarding call, it updates to v2. Notice all 10 tasks completed successfully."

---

### SECTION 3: Task Tracker (1:30 - 1:45)

**Action:** Show the task tracker file:

```bash
type outputs\tasks.json
```

Or open `outputs/tasks.json` in VS Code.

**Say:** "The task tracker captures each processing step. We have 10 tasks - 5 for demo processing (v1) and 5 for onboarding updates (v2). All are marked as completed."

---

### SECTION 4: Dashboard (1:45 - 2:00)

**Action:** Generate and open the dashboard:

```bash
python scripts/dashboard.py
```

Then open `outputs/dashboard.html` in your browser.

**Say:** "The dashboard provides a visual overview. It shows all 5 accounts, their v1 and v2 status, services supported, and recent changes. This gives a quick snapshot of the entire pipeline."

---

### SECTION 5: Diff Viewer (2:00 - 2:30)

**Action:** Run the diff viewer:

```bash
python scripts/diff_viewer.py ben001
```

**What to show:**
- The terminal output showing v1 → v2 changes
- Highlight the "services_supported" change
- Show the changelog section

**Say:** "The diff viewer shows exactly what changed between v1 and v2. For example, here we can see the services_supported were updated from the demo version to the onboarding version. The changelog tracks all these modifications."

---

### SECTION 6: Generated Files (2:30 - 3:30)

**Action:** Open these files in VS Code and show them one by one:

1. **v1 Account Memo:**
   ```
   outputs/accounts/ben001/v1/account_memo.json
   ```
   **Say:** "This is the structured account memo generated from the demo call. It contains company info, business hours, services, emergency rules, and more."

2. **v1 Retell Agent Spec:**
   ```
   outputs/accounts/ben001/v1/retell_agent_spec.json
   ```
   **Say:** "This is the Retell agent specification - the actual configuration we'd import into Retell. It includes the system prompt, key variables, and call transfer protocols."

3. **v2 Account Memo:**
   ```
   outputs/accounts/ben001/v2/account_memo.json
   ```
   **Say:** "After onboarding, the account memo is updated with new information."

4. **Changelog:**
   ```
   outputs/accounts/ben001/v2/changelog_v2.json
   ```
   **Say:** "The changelog tracks what changed from v1 to v2 - in this case, services were updated."

---

### SECTION 7: Agent Simulation (3:30 - 4:00)

**Action:** Run the simulation:

```bash
python scripts/simulate_call_v2_import.py
```

**What to show:**
- The simulated call handling
- Business hours routing
- Emergency vs non-emergency flows

**Say:** "Here's a simulation of the agent handling a call. It uses the v2 configuration to route the caller appropriately, check business hours, and handle the request."

---

### SECTION 8: Closing (4:00 - 4:30)

**Action:** Return to terminal and summarize.

**Say:** "To summarize, this pipeline:
1. Takes demo call transcripts and generates v1 agent configurations
2. Takes onboarding info and creates v2 updates
3. Maintains version history with changelogs
4. Provides task tracking with visual dashboards

All running with zero cost - no paid APIs required. Thank you!"

---

## Terminal Commands Summary

Copy-paste this sequence for your recording:

```bash
# 1. Show structure
dir /b

# 2. Run batch processing
python scripts/batch_process.py

# 3. Show task tracker
type outputs\tasks.json

# 4. Generate dashboard
python scripts/dashboard.py

# 5. Show diff
python scripts/diff_viewer.py ben001

# 6. Simulate call
python scripts/simulate_call_v2_import.py
```

---

## Tips for a Great Recording

### Do:
- ✅ Speak clearly and at a moderate pace
- ✅ Highlight key outputs (account_memo, agent_spec, changelog)
- ✅ Show the v1 → v2 transition clearly
- ✅ Keep it under 5 minutes
- ✅ Use cursor to point at important items

### Don't:
- ❌ Read every line of code
- ❌ Go too fast through important parts
- ❌ Forget to show the changelog
- ❌ Skip the agent simulation

---

## After Recording

1. **Trim** any mistakes using Loom's editor
2. **Add a title**: "Clara Answers Pipeline Demo"
3. **Add a description**: Brief summary of what you demonstrated
4. **Copy the link** and add it to README.md

---

## Need Help?

If you need to re-record:
1. Delete the old video from Loom
2. Clear outputs if needed: `rmdir /s outputs\accounts` (careful!)
3. Re-run: `python scripts/batch_process.py`
4. Record again following this script

---

**Good luck with your recording!**


