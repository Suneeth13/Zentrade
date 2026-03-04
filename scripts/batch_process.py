"""
Batch Processing Script for Clara Answers Pipeline
Processes all demo and onboarding transcripts to generate account memos and agent specs.
"""
import json
import os
from datetime import datetime

# Base paths
BASE_DIR = "D:/Zentrade"
DATASET_DIR = f"{BASE_DIR}/dataset"
OUTPUTS_DIR = f"{BASE_DIR}/outputs/accounts"
TASKS_FILE = f"{BASE_DIR}/outputs/tasks.json"

# Demo call mappings (demo file -> account ID -> company name)
# Note: transcript.txt is in data/raw/, demo2-5 are in dataset/demo/
DEMO_MAPPINGS = {
    "transcript.txt": ("ben001", "Ben's Electric Solutions"),
    "demo2.txt": ("plum001", "Mike's Plumbing Services"),
    "demo3.txt": ("med001", "GreenLeaf Medical Clinic"),
    "demo4.txt": ("tech001", "TechPro Solutions LLC"),
    "demo5.txt": ("prop001", "Santos Property Management"),
}

# Onboarding call mappings
ONBOARD_MAPPINGS = {
    "onboard1.txt": "ben001",
    "onboard2.txt": "plum001",
    "onboard3.txt": "med001",
    "onboard4.txt": "tech001",
    "onboard5.txt": "prop001",
}

def load_tasks():
    """Load existing tasks or create new list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "summary": {"total": 0, "completed": 0, "pending": 0}}

def save_tasks(tasks_data):
    """Save tasks to file."""
    os.makedirs(f"{BASE_DIR}/outputs", exist_ok=True)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks_data, f, indent=2)

def create_task(account_id, task_type, status="pending", details=""):
    """Create a new task."""
    return {
        "id": f"task_{account_id}_{task_type}",
        "account_id": account_id,
        "type": task_type,
        "status": status,
        "details": details,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

def extract_info_from_transcript(transcript_text):
    """Extract key information from transcript text using rule-based extraction."""
    lines = transcript_text.lower()
    
    business_hours = {"days": ["Mon", "Tue", "Wed", "Thu", "Fri"], "start": "09:00", "end": "18:00", "timezone": "PST"}
    
    if "7 am" in lines: business_hours["start"] = "07:00"
    if "8 am" in lines: business_hours["start"] = "08:00"
    if "5 pm" in lines: business_hours["end"] = "17:00"
    if "6 pm" in lines: business_hours["end"] = "18:00"
    
    services = []
    if "plumb" in lines: services.append("Plumbing")
    if "hvac" in lines or "ac" in lines: services.append("HVAC")
    if "it" in lines or "tech" in lines: services.append("IT Support")
    if "medical" in lines or "clinic" in lines: services.append("Medical")
    if "property" in lines or "maintenance" in lines: services.append("Property Management")
    if not services: services = ["General Service"]
    
    emergency_definition = []
    if "outage" in lines or "no hot water" in lines: emergency_definition.append("Utility Outage")
    if "flood" in lines or "leak" in lines: emergency_definition.append("Water Leak")
    if "ac" in lines and "heat" in lines: emergency_definition.append("AC Out in Heat")
    if "security" in lines or "breach" in lines: emergency_definition.append("Security Breach")
    
    return {"business_hours": business_hours, "services_supported": services, "emergency_definition": emergency_definition}

def create_account_memo(account_id, company_name, extracted_info, version="v1", notes=""):
    """Create account memo JSON."""
    return {
        "account_id": account_id,
        "company_name": company_name,
        "business_hours": extracted_info["business_hours"],
        "office_address": "See account notes",
        "services_supported": extracted_info["services_supported"],
        "emergency_definition": extracted_info["emergency_definition"] or ["Urgent Issue"],
        "emergency_routing_rules": ["Transfer to on-call technician", "Leave message if no answer"],
        "non_emergency_routing_rules": ["Schedule callback", "Create work order"],
        "call_transfer_rules": {"timeouts": "30s", "retries": 2, "fallback": "Leave message and notify via SMS"},
        "integration_constraints": [],
        "after_hours_flow_summary": "Greet, confirm emergency, collect info, attempt transfer, fallback to voicemail",
        "office_hours_flow_summary": "Greet, collect info, transfer to agent, confirm next steps",
        "questions_or_unknowns": [],
        "notes": notes
    }

def create_agent_spec(account_id, company_name, extracted_info, version="v1"):
    """Create Retell agent spec JSON."""
    business_hours = extracted_info["business_hours"]
    services = extracted_info["services_supported"]
    days = "-".join(business_hours["days"])
    
    system_prompt = f"You are an automated assistant for {company_name}. "
    system_prompt += f"Business hours are {days} {business_hours['start']} to {business_hours['end']}. "
    system_prompt += "During business hours, greet caller, collect name/number, determine purpose, route to agent. "
    system_prompt += "After hours, confirm emergency, collect info, attempt transfer, fallback to voicemail."
    
    return {
        "agent_name": f"{company_name.split()[0]}Agent",
        "voice_style": "basic",
        "system_prompt": system_prompt,
        "key_variables": {
            "timezone": business_hours["timezone"],
            "business_hours": business_hours,
            "office_address": "See account notes",
            "emergency_routing_rules": ["Transfer to on-call", "SMS notification"],
            "non_emergency_routing_rules": ["Schedule callback", "Create work order"],
            "services_supported": services
        },
        "tool_invocation_placeholders": [],
        "call_transfer_protocol": {"timeouts": "30s", "retries": 2, "fallback": "Leave message and notify via SMS"},
        "fallback_protocol_if_transfer_fails": "Leave message and send SMS notification",
        "version": version
    }

def create_changelog(account_id, version_from, version_to, changes):
    """Create changelog JSON."""
    return {
        "account_id": account_id,
        "version_from": version_from,
        "version_to": version_to,
        "changes": changes,
        "timestamp": datetime.now().isoformat(),
        "notes": "Generated from onboarding info"
    }

def process_demo_call(demo_file, account_id, company_name):
    """Process a demo call transcript and generate v1 assets."""
    print(f"\n{'='*60}")
    print(f"Processing Demo Call: {demo_file}")
    print(f"Account: {account_id} - {company_name}")
    print(f"{'='*60}")
    
    with open(f"{DATASET_DIR}/demo/{demo_file}", "r") as f:
        transcript = f.read()
    
    extracted_info = extract_info_from_transcript(transcript)
    account_dir = f"{OUTPUTS_DIR}/{account_id}/v1"
    os.makedirs(account_dir, exist_ok=True)
    
    memo = create_account_memo(account_id, company_name, extracted_info, version="v1", notes=f"Created from demo: {demo_file}")
    agent_spec = create_agent_spec(account_id, company_name, extracted_info, version="v1")
    
    with open(f"{account_dir}/account_memo.json", "w") as f:
        json.dump(memo, f, indent=2)
    with open(f"{account_dir}/retell_agent_spec.json", "w") as f:
        json.dump(agent_spec, f, indent=2)
    
    print(f"✓ Created v1 account memo and agent spec")
    print(f"  Services: {', '.join(extracted_info['services_supported'])}")
    return account_id

def process_onboarding_call(onboard_file, account_id):
    """Process an onboarding call transcript and generate v2 assets."""
    print(f"\n{'='*60}")
    print(f"Processing Onboarding Call: {onboard_file}")
    print(f"Account: {account_id}")
    print(f"{'='*60}")
    
    with open(f"{DATASET_DIR}/onboarding/{onboard_file}", "r") as f:
        transcript = f.read()
    
    extracted_info = extract_info_from_transcript(transcript)
    v1_memo_path = f"{OUTPUTS_DIR}/{account_id}/v1/account_memo.json"
    
    if os.path.exists(v1_memo_path):
        with open(v1_memo_path, "r") as f:
            v1_memo = json.load(f)
        original_company = v1_memo.get("company_name", account_id)
    else:
        original_company = account_id
    
    v2_dir = f"{OUTPUTS_DIR}/{account_id}/v2"
    os.makedirs(v2_dir, exist_ok=True)
    
    v2_memo = create_account_memo(account_id, original_company, extracted_info, version="v2", notes=f"Updated from: {onboard_file}")
    v2_agent_spec = create_agent_spec(account_id, original_company, extracted_info, version="v2")
    
    changes = [{"field": "services_supported", "old_value": v1_memo.get("services_supported", []), "new_value": extracted_info["services_supported"], "description": "Updated services from onboarding"}]
    changelog = create_changelog(account_id, "v1", "v2", changes)
    
    with open(f"{v2_dir}/account_memo.json", "w") as f:
        json.dump(v2_memo, f, indent=2)
    with open(f"{v2_dir}/retell_agent_spec.json", "w") as f:
        json.dump(v2_agent_spec, f, indent=2)
    with open(f"{v2_dir}/changelog_v2.json", "w") as f:
        json.dump(changelog, f, indent=2)
    
    print(f"✓ Created v2 account memo, agent spec, and changelog")
    print(f"  Services: {', '.join(extracted_info['services_supported'])}")
    return True

def main():
    """Main batch processing function."""
    print("\n" + "="*70)
    print("CLARA ANSWERS PIPELINE - BATCH PROCESSOR")
    print("="*70)
    print(f"\nProcessing time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Initialize tasks
    tasks_data = load_tasks()
    tasks_data["tasks"] = []
    
    # Phase 1: Demo calls
    print("\n" + "="*70)
    print("PHASE 1: Processing Demo Calls (Generating v1)")
    print("="*70)
    
    for demo_file, (account_id, company_name) in DEMO_MAPPINGS.items():
        try:
            process_demo_call(demo_file, account_id, company_name)
            # Create task
            tasks_data["tasks"].append(create_task(account_id, "demo_v1", "completed", f"Processed {demo_file}"))
        except Exception as e:
            print(f"✗ Error: {e}")
            tasks_data["tasks"].append(create_task(account_id, "demo_v1", "failed", str(e)))
    
    # Phase 2: Onboarding calls
    print("\n" + "="*70)
    print("PHASE 2: Processing Onboarding Calls (Generating v2)")
    print("="*70)
    
    for onboard_file, account_id in ONBOARD_MAPPINGS.items():
        try:
            process_onboarding_call(onboard_file, account_id)
            tasks_data["tasks"].append(create_task(account_id, "onboarding_v2", "completed", f"Processed {onboard_file}"))
        except Exception as e:
            print(f"✗ Error: {e}")
            tasks_data["tasks"].append(create_task(account_id, "onboarding_v2", "failed", str(e)))
    
    # Update summary
    tasks_data["summary"]["total"] = len(tasks_data["tasks"])
    tasks_data["summary"]["completed"] = sum(1 for t in tasks_data["tasks"] if t["status"] == "completed")
    tasks_data["summary"]["pending"] = sum(1 for t in tasks_data["tasks"] if t["status"] == "pending")
    save_tasks(tasks_data)
    
    # Summary
    print("\n" + "="*70)
    print("BATCH PROCESSING COMPLETE")
    print("="*70)
    print(f"\nTasks created: {tasks_data['summary']['total']}")
    print(f"Completed: {tasks_data['summary']['completed']}")
    print(f"Failed: {tasks_data['summary']['total'] - tasks_data['summary']['completed']}")
    print(f"\nTasks saved to: {TASKS_FILE}")

if __name__ == "__main__":
    main()

