import json
from datetime import datetime

# --- Load v2 imported JSON ---
import_json_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_v2_import.json"

with open(import_json_path, "r") as f:
    import_data = json.load(f)

agent_spec = import_data["agent_spec"]
account_memo = import_data["account_memo"]

# Extract info
business_hours = agent_spec["key_variables"]["business_hours"]
primary_contact = agent_spec["key_variables"].get("primary_contact", {})
services_supported = agent_spec["key_variables"].get("services_supported", [])
company_address = agent_spec["key_variables"].get("office_address", "")

transfer_rules = agent_spec["call_transfer_protocol"]
fallback = agent_spec["fallback_protocol_if_transfer_fails"]

# Helper function to check if current time is within business hours
def is_business_hour():
    now = datetime.now()
    current_day = now.strftime("%a")  # e.g., Mon, Tue
    current_time = now.strftime("%H:%M")
    if current_day in business_hours["days"]:
        if business_hours["start"] <= current_time <= business_hours["end"]:
            return True
    return False

# Simulate a call automatically
def simulate_call():
    print("=== Incoming Call ===")
    
    # Use imported JSON data automatically
    caller_name = primary_contact.get("name", "")
    caller_phone = primary_contact.get("phone", "")
    purpose = services_supported[0] if services_supported else ""
    
    # Track unknown or missing info
    questions_or_unknowns = []
    if not caller_name:
        questions_or_unknowns.append("Caller name missing")
    if not caller_phone:
        questions_or_unknowns.append("Caller phone missing")
    if purpose.lower() not in [s.lower() for s in services_supported]:
        questions_or_unknowns.append(f"Purpose '{purpose}' not recognized")
    
    # Add to account memo
    account_memo['questions_or_unknowns'] = questions_or_unknowns

    print("\n--- Agent Response ---")
    if is_business_hour():
        print(f"Greeting! This is {agent_spec['agent_name']} for {account_memo['company_name']}.")
        print(f"Collecting info: Name: {caller_name or 'Unknown'}, Phone: {caller_phone or 'Unknown'}")
        if purpose:
            print(f"Purpose identified as '{purpose}'. Routing to the correct agent.")
        else:
            print("Purpose not provided. Need clarification.")
        print("Next steps confirmed. Thank you!")
    else:
        print("After hours call detected.")
        print(f"Confirming emergency for purpose: {purpose or 'Unknown'}")
        if purpose.lower() in [e.lower() for e in account_memo.get("emergency_definition", [])]:
            print("Emergency detected! Attempting transfer...")
            for attempt in range(1, transfer_rules["retries"] + 1):
                print(f"Transfer attempt {attempt}...")
            print(f"Fallback activated: {fallback}")
        else:
            print("Non-emergency after hours. Recording info and assuring callback next business day.")

    print("\n--- Call Summary ---")
    print(f"Caller: {caller_name or 'Unknown'}, Phone: {caller_phone or 'Unknown'}")
    print(f"Purpose: {purpose or 'Unknown'}")
    print(f"Handled by: {agent_spec['agent_name']}")
    print(f"Business Hours: {business_hours['days'][0]}-{business_hours['days'][-1]}, "
          f"{business_hours['start']}-{business_hours['end']} {agent_spec['key_variables']['timezone']}")
    
    # Save updated account memo with questions_or_unknowns
    output_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo_updated.json"
    with open(output_path, "w") as f:
        json.dump(account_memo, f, indent=4)
    print(f"\nUpdated account memo saved to {output_path}")

if __name__ == "__main__":
    simulate_call()