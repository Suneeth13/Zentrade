import json

# Paths
memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
changelog_path = "D:/Zentrade/outputs/accounts/ben001/v2/changelog_v2.json"
chat_path = "D:/Zentrade/outputs/accounts/ben001/chat.txt"
recording_path = "D:/Zentrade/outputs/accounts/ben001/recording.conf"

# Load JSONs
with open(memo_path, "r") as f:
    account_memo = json.load(f)

with open(agent_path, "r") as f:
    agent_spec = json.load(f)

with open(changelog_path, "r") as f:
    changelog = json.load(f)

# Load chat.txt
with open(chat_path, "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Extract caller info
caller_email = lines[0].split(":")[-1].strip()
service_requested = lines[1].split(":")[-1].strip()
caller_name = lines[2].split(":")[-1].strip()
caller_phone = lines[3].split(":")[-1].strip()
confirmation_email = lines[4].split(":")[-1].strip()

# Load recording.conf
with open(recording_path, "r") as f:
    recording = json.load(f)

audio_file = recording['items'][0]['audio']
video_file = recording['items'][0]['video']

# Initialize RetellAgent class
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
        print("\n=== Simulated Call from chat.txt with recordings ===\n")
        print(f"Incoming call from {caller_name} ({caller_phone}) requesting {service_requested}")
        print(f"Agent Response: Hello {caller_name}, thank you for contacting Ben's Electric Solutions.")
        print(f"We support {', '.join(self.key_vars.get('services_supported', []))}. Your request for {service_requested} will be handled shortly.")
        print(f"Confirmation will be sent to {confirmation_email}.")
        print(f"Audio recording: {audio_file}, Video recording: {video_file}\n")
        print("--------------------------------------------------\n")
        print("=== Account Memo Summary ===")
        print(f"Account ID: {self.memo['account_id']}")
        print(f"Primary Contact: {self.memo.get('notes', 'N/A')}")
        print(f"Services Supported: {self.memo['services_supported']}")
        print(f"Company Address: {self.memo['office_address']}\n")
        print("=== Changelog ===")
        print(changelog)

# Create agent instance
agent = RetellAgent(agent_spec, account_memo)

# Print summary + simulated call
agent.summary()