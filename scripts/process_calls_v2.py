import json

# Paths
memo_path = "D:/Zentrade/outputs/accounts/ben001/v2/account_memo.json"
agent_path = "D:/Zentrade/outputs/accounts/ben001/v2/retail_agent_spec_v2.json"
chat_path = "D:/Zentrade/outputs/accounts/ben001/chat.txt"
recording_conf_path = "D:/Zentrade/outputs/accounts/ben001/recording.conf"
changelog_path = "D:/Zentrade/outputs/accounts/ben001/v2/changelog_v2.json"

# ---- Step 1: Read chat.txt ----
with open(chat_path, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Extract the part after the last colon
service_requested = lines[1].split(":")[-1].strip()
caller_name = lines[2].split(":")[-1].strip()
caller_phone = lines[3].split(":")[-1].strip()
caller_email = lines[4].split(":")[-1].strip()
# ---- Step 2: Read recording.conf ----
with open(recording_conf_path, "r") as f:
    recording_data = json.load(f)

audio_file = recording_data["items"][0]["audio"]
video_file = recording_data["items"][0]["video"]

# ---- Step 3: Read account memo & changelog ----
with open(memo_path, "r") as f:
    account_memo = json.load(f)

with open(changelog_path, "r") as f:
    changelog = json.load(f)

# ---- Step 4: Simulate the call ----
print("=== Simulated Call from chat.txt with recordings ===\n")
print(f"Incoming call from {caller_name} ({caller_phone}) requesting {service_requested}")
print(f"Agent Response: Hello {caller_name}, thank you for contacting {account_memo['company_name']}.")
print(f"We support {', '.join(account_memo['services_supported'])}. Your request for {service_requested} will be handled shortly.")
print(f"Confirmation will be sent to {caller_email}.")
print(f"Audio recording: {audio_file}, Video recording: {video_file}")
print("\n" + "-"*50 + "\n")

# ---- Step 5: Account memo summary ----
print("=== Account Memo Summary ===")
print(f"Account ID: {account_memo['account_id']}")
print(f"Primary Contact: {account_memo.get('primary_contact', account_memo.get('notes', 'N/A'))}")
print(f"Services Supported: {account_memo['services_supported']}")
print(f"Company Address: {account_memo['office_address']}")

# ---- Step 6: Changelog ----
print("\n=== Changelog ===")
print(changelog)