import json
from datetime import datetime

# Load v2 JSON files

memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"

with open(memo_path, "r") as f:
    account_memo = json.load(f)

with open(agent_path, "r") as f:
    agent_spec = json.load(f)

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

# Simulate a call
def simulate_call():
    print("=== Incoming Call ===")
    caller_name = input("Caller Name: ")
    caller_phone = input("Caller Phone: ")
    purpose = input("Purpose of Call: ")

    print("\n--- Agent Response ---")
    if is_business_hour():
        print(f"Greeting! This is {agent_spec['agent_name']} for {account_memo['company_name']}.")
        print(f"Collecting info: Name: {caller_name}, Phone: {caller_phone}")
        if purpose.lower() in [s.lower() for s in services_supported]:
            print(f"Purpose identified as '{purpose}'. Routing to the correct agent.")
        else:
            print(f"Purpose '{purpose}' not recognized. Provide assistance or note query.")
        print(f"Next steps confirmed. Thank you!")
    else:
        print("After hours call detected.")
        print(f"Confirming emergency for purpose: {purpose}")
        if purpose.lower() in [e.lower() for e in account_memo["emergency_definition"]]:
            print("Emergency detected! Attempting transfer...")
            for attempt in range(1, transfer_rules["retries"] + 1):
                print(f"Transfer attempt {attempt}...")
            print(f"Fallback activated: {fallback}")
        else:
            print("Non-emergency after hours. Recording info and assuring callback next business day.")

    print("\n--- Call Summary ---")
    print(f"Caller: {caller_name}, Phone: {caller_phone}")
    print(f"Purpose: {purpose}")
    print(f"Handled by: {agent_spec['agent_name']}")
    print(f"Business Hours: {business_hours['days'][0]}-{business_hours['days'][-1]}, {business_hours['start']}-{business_hours['end']} {agent_spec['key_variables']['timezone']}")

if __name__ == "__main__":
    simulate_call()