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
    chat_lines = [line.strip() for line in f if line.strip()]

# Extract info from chat.txt
caller_email = chat_lines[0].split(":")[-1].strip()
service_request = chat_lines[1].split(":")[-1].strip()
caller_name = chat_lines[2].split(":")[-1].strip()
caller_phone = chat_lines[3].split(":")[-1].strip()
confirmation_email = chat_lines[4].split(":")[-1].strip()

# Load recording.conf
with open(recording_path, "r") as f:
    recording_conf = json.load(f)

audio_file = recording_conf["items"][0]["audio"]
video_file = recording_conf["items"][0]["video"]

# Define RetellAgent class
class RetellAgent:
    def __init__(self, spec, memo):
        self.name = spec.get("agent_name")
        self.voice_style = spec.get("voice_style")
        self.system_prompt = spec.get("system_prompt")
        self.key_vars = spec.get("key_variables", {})
        self.memo = memo

    def summary(self):
        print("=== Account Memo Summary ===")
        print(f"Account ID: {self.memo['account_id']}")
        print(f"Primary Contact: {self.key_vars.get('primary_contact', 'N/A')}")
        print(f"Services Supported: {self.key_vars.get('services_supported', [])}")
        print(f"Company Address: {self.key_vars.get('office_address', 'N/A')}\n")

    def handle_call(self, caller_name, caller_phone, service_request, confirmation_email, audio_file, video_file):
        print("=== Simulated Call from chat.txt with recordings ===\n")
        print(f"Incoming call from {caller_name} ({caller_phone}) requesting {service_request}")
        print(f"Agent Response: Hello {caller_name}, thank you for contacting {self.memo['company_name']}.")
        print(f"We support {', '.join(self.memo['services_supported'])}. Your request for {service_request} will be handled shortly.")
        print(f"Confirmation will be sent to {confirmation_email}.")
        print(f"Audio recording: {audio_file}, Video recording: {video_file}\n")
        print("--------------------------------------------------\n")

# Initialize agent
agent = RetellAgent(agent_spec, account_memo)

# Print agent summary
agent.summary()

# Simulate the call
agent.handle_call(caller_name, caller_phone, service_request, confirmation_email, audio_file, video_file)

# Print changelog
print("=== Changelog ===")
print(changelog)