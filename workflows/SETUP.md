# n8n Workflow Setup Guide

## Prerequisites
- Docker Desktop installed on your machine
- At least 4GB RAM available

## Quick Start

### 1. Start n8n Container
```bash
cd d:/Zentrade
docker-compose up -d
```

### 2. Access n8n
- Open browser: http://localhost:5678
- Login credentials:
  - Username: admin
  - Password: clara123

### 3. Import Workflow

#### Option A: Import JSON File
1. In n8n, click "Workflows" → "Import from File"
2. Select `workflows/clara_answers_pipeline.json`
3. Click "Import"

#### Option B: Manual Setup
If you prefer to create manually:

1. **Create new workflow**
2. **Add nodes** (in order):
   - Schedule Trigger (every 5 minutes)
   - Read Binary File (demo transcripts)
   - Code Node (Extract Info)
   - Code Node (Generate Account Memo)
   - Code Node (Generate Agent Spec)
   - Write Binary File (save memo)
   - Write Binary File (save agent spec)
   - Code Node (Generate Changelog - for v2)
   - Write Binary File (save changelog)

3. **Connect nodes** as shown in the JSON

### 4. Configure File Paths

Update these paths in the workflow to match your setup:
- Demo transcripts: `D:/Zentrade/dataset/demo`
- Onboarding transcripts: `D:/Zentrade/dataset/onboarding`
- Outputs: `D:/Zentrade/outputs/accounts`

### 5. Activate Workflow
Click the toggle button to activate the workflow.

## Testing the Workflow

### Manual Test
1. Add a new transcript file to `dataset/demo/` or `dataset/onboarding/`
2. The workflow will pick it up on next run
3. Check `outputs/accounts/` for generated files

### Run Batch Script Instead
For immediate results without waiting:
```bash
python scripts/batch_process.py
```

## Workflow Nodes Overview

| Node | Purpose |
|------|---------|
| Schedule Trigger | Runs every 5 minutes |
| Read Binary File | Reads transcript files |
| Extract Info | Rule-based extraction of business hours, services, emergencies |
| Generate Account Memo | Creates structured account JSON |
| Generate Agent Spec | Creates Retell agent configuration |
| Save Files | Writes outputs to disk |
| Generate Changelog | Creates version diff for v2 |

## Customization

### Add New Account Types
Edit the extraction logic in the "Extract Info from Transcript" code node to recognize new business types.

### Modify Agent Prompts
Edit the "Generate Agent Spec" code node to customize the system prompt template.

### Add Integrations
Add new nodes for:
- Send email notifications
- Create Asana tasks
- Post to Slack
- Call Retell API

## Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs n8n

# Restart
docker-compose restart
```

### Workflow not triggering
- Check that the workflow is "Active" (toggle is on)
- Verify file paths are correct
- Check n8n execution logs

### Files not being created
- Verify write permissions on output directories
- Check Docker volume mounts

## Stopping the Pipeline
```bash
docker-compose down
```

## Next Steps
1. Customize the extraction logic for your specific needs
2. Add webhook integrations for real-time processing
3. Connect to Retell API (requires paid account)
4. Add monitoring and alerting

