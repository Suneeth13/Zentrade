import json

# Paths to existing files
agent_spec_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
account_memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
changelog_path = "D:/Zentrade/outputs/accounts/ben001/v2/changelog_v2.json"
recording_conf_path = "D:/Zentrade/outputs/accounts/ben001/recording.conf"

# Load JSON files
with open(agent_spec_path, "r") as f:
    agent_spec = json.load(f)

with open(account_memo_path, "r") as f:
    account_memo = json.load(f)

with open(changelog_path, "r") as f:
    changelog = json.load(f)

with open(recording_conf_path, "r") as f:
    recording_conf = json.load(f)

# Combine everything into one import-ready JSON
agent_import = {
    "agent_spec": agent_spec,
    "account_memo": account_memo,
    "changelog": changelog,
    "recordings": recording_conf
}

# Save the import-ready JSON
output_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_v2_import.json"
with open(output_path, "w") as f:
    json.dump(agent_import, f, indent=4)

print(f"v2 agent import JSON created successfully at:\n{output_path}")