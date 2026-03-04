import json

# Correct Paths
memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
changelog_path = "D:/Zentrade/outputs/accounts/ben001/v2/changelog_v2.json"

# Load JSON files
with open(memo_path, "r") as f:
    account_memo = json.load(f)

with open(agent_path, "r") as f:
    agent_spec = json.load(f)

with open(changelog_path, "r") as f:
    changelog = json.load(f)

# Print summaries
print("=== Account Memo Summary ===")
print(f"Account ID: {account_memo['account_id']}")
print(f"Company: {account_memo['company_name']}")
print(f"Services: {account_memo['services_supported']}")
print(f"Primary Contact: {agent_spec['key_variables'].get('primary_contact', 'N/A')}")

print("\n=== Changelog ===")
print(changelog)