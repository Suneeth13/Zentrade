import json

# Path to imported agent JSON
import_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_v2_import.json"

# Load the JSON
with open(import_path, "r") as f:
    agent_v2_data = json.load(f)

# Extract the agent spec
agent_spec = agent_v2_data["agent_spec"]
key_vars = agent_spec.get("key_variables", {})
account_memo = agent_v2_data["account_memo"]

# Print agent summary
print("=== Imported v2 Agent ===")
print(f"Agent Name: {agent_spec.get('agent_name')}")
print(f"Voice Style: {agent_spec.get('voice_style')}")
print(f"Primary Contact: {key_vars.get('primary_contact', 'N/A')}")
print(f"Services Supported: {key_vars.get('services_supported', [])}")
print(f"Company Address: {key_vars.get('office_address', 'N/A')}")

# Optional: print account memo summary
print("\n=== Account Memo Summary ===")
print(f"Account ID: {account_memo.get('account_id')}")
print(f"Primary Contact: {account_memo.get('primary_contact', 'N/A')}")
print(f"Services Supported: {account_memo.get('services_supported', [])}")
print(f"Company Address: {account_memo.get('office_address', 'N/A')}")