"""
Diff Viewer - Shows differences between v1 and v2 agent configurations
"""
import json
import os

BASE_DIR = "D:/Zentrade"
ACCOUNTS_DIR = f"{BASE_DIR}/outputs/accounts"

def load_json(path):
    """Load JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def compare_dicts(d1, d2, path=""):
    """Recursively compare two dictionaries and return differences."""
    differences = []
    
    all_keys = set(d1.keys()) | set(d2.keys())
    
    for key in all_keys:
        current_path = f"{path}.{key}" if path else key
        
        if key not in d1:
            differences.append({"path": current_path, "type": "added", "value": d2[key]})
        elif key not in d2:
            differences.append({"path": current_path, "type": "removed", "value": d1[key]})
        elif d1[key] != d2[key]:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                differences.extend(compare_dicts(d1[key], d2[key], current_path))
            else:
                differences.append({"path": current_path, "type": "changed", "old_value": d1[key], "new_value": d2[key]})
    
    return differences

def show_diff(account_id):
    """Show diff for a specific account."""
    v1_memo_path = f"{ACCOUNTS_DIR}/{account_id}/v1/account_memo.json"
    v2_memo_path = f"{ACCOUNTS_DIR}/{account_id}/v2/account_memo.json"
    v1_agent_path = f"{ACCOUNTS_DIR}/{account_id}/v1/retell_agent_spec.json"
    v2_agent_path = f"{ACCOUNTS_DIR}/{account_id}/v2/retell_agent_spec.json"
    
    print(f"\n{'='*70}")
    print(f"DIFF VIEWER - Account: {account_id}")
    print(f"{'='*70}")
    
    # Compare Account Memos
    if os.path.exists(v1_memo_path) and os.path.exists(v2_memo_path):
        print(f"\n--- Account Memo Changes (v1 → v2) ---")
        v1_memo = load_json(v1_memo_path)
        v2_memo = load_json(v2_memo_path)
        
        diffs = compare_dicts(v1_memo, v2_memo)
        
        if diffs:
            for d in diffs:
                if d["type"] == "added":
                    print(f"  + {d['path']}: {d['value']}")
                elif d["type"] == "removed":
                    print(f"  - {d['path']}: {d['value']}")
                elif d["type"] == "changed":
                    print(f"  ~ {d['path']}:")
                    print(f"      old: {d['old_value']}")
                    print(f"      new: {d['new_value']}")
        else:
            print("  No changes in account memo")
    
    # Compare Agent Specs
    if os.path.exists(v1_agent_path) and os.path.exists(v2_agent_path):
        print(f"\n--- Agent Spec Changes (v1 → v2) ---")
        v1_agent = load_json(v1_agent_path)
        v2_agent = load_json(v2_agent_path)
        
        diffs = compare_dicts(v1_agent, v2_agent)
        
        if diffs:
            for d in diffs:
                if d["type"] == "added":
                    print(f"  + {d['path']}: {d['value']}")
                elif d["type"] == "removed":
                    print(f"  - {d['path']}: {d['value']}")
                elif d["type"] == "changed":
                    print(f"  ~ {d['path']}:")
                    print(f"      old: {d['old_value']}")
                    print(f"      new: {d['new_value']}")
        else:
            print("  No changes in agent spec")
    
    # Show changelog
    changelog_path = f"{ACCOUNTS_DIR}/{account_id}/v2/changelog_v2.json"
    if os.path.exists(changelog_path):
        print(f"\n--- Changelog ---")
        changelog = load_json(changelog_path)
        for change in changelog.get("changes", []):
            print(f"  • {change.get('description', 'Updated')}")
            if "field" in change:
                print(f"    Field: {change['field']}")

def list_accounts():
    """List all accounts with v1 and v2."""
    print("\nAvailable Accounts:")
    for d in os.listdir(ACCOUNTS_DIR):
        v1_exists = os.path.exists(f"{ACCOUNTS_DIR}/{d}/v1")
        v2_exists = os.path.exists(f"{ACCOUNTS_DIR}/{d}/v2")
        status = []
        if v1_exists: status.append("v1")
        if v2_exists: status.append("v2")
        print(f"  - {d}: {', '.join(status) if status else 'no outputs'}")

def main():
    """Main function."""
    import sys
    
    if len(sys.argv) > 1:
        account_id = sys.argv[1]
    else:
        list_accounts()
        account_id = input("\nEnter account ID: ").strip()
    
    if account_id:
        show_diff(account_id)

if __name__ == "__main__":
    main()

