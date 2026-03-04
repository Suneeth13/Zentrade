import json

# Correct Paths
memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
changelog_path = "D:/Zentrade/outputs/accounts/ben001/v2/changelog_v2.json"

# Load JSONs
with open(memo_path, "r") as f:
    account_memo = json.load(f)

with open(agent_path, "r") as f:
    agent_spec = json.load(f)

with open(changelog_path, "r") as f:
    changelog = json.load(f)

# Initialize agent (simplified)
class RetellAgent:
    def __init__(self, spec, memo):
        self.name = spec.get("agent_name")
        self.voice_style = spec.get("voice_style")
        self.system_prompt = spec.get("system_prompt")
        self.key_vars = spec.get("key_variables", {})
        self.memo = memo

    def summary(self):
        print(f"Agent Name: {self.name}")
        print(f"Voice Style: {self.voice_style}")
        print(f"Primary Contact: {self.key_vars.get('primary_contact', 'N/A')}")
        print(f"Services Supported: {self.key_vars.get('services_supported', [])}")
        print(f"Company Address: {self.key_vars.get('office_address', 'N/A')}")

# Create agent instance
agent = RetellAgent(agent_spec, account_memo)

# Print summary
agent.summary()