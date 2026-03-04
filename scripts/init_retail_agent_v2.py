import json

# Paths
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"

# Load JSONs
with open(agent_path, "r") as f:
    agent_spec = json.load(f)

with open(memo_path, "r") as f:
    account_memo = json.load(f)

# RetellAgent class
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

# Initialize agent
agent = RetellAgent(agent_spec, account_memo)

# Print summary (ready for import)
agent.summary()