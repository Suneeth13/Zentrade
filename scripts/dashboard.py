"""
Simple Dashboard - HTML-based UI for the Clara Answers Pipeline
"""
import json
import os
from datetime import datetime

BASE_DIR = "D:/Zentrade"
ACCOUNTS_DIR = f"{BASE_DIR}/outputs/accounts"
TASKS_FILE = f"{BASE_DIR}/outputs/tasks.json"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def get_account_data():
    """Get data for all accounts."""
    accounts = []
    
    if not os.path.exists(ACCOUNTS_DIR):
        return accounts
    
    for account_id in os.listdir(ACCOUNTS_DIR):
        account_path = f"{ACCOUNTS_DIR}/{account_id}"
        if not os.path.isdir(account_path):
            continue
        
        data = {"account_id": account_id}
        
        # Check v1
        v1_memo_path = f"{account_path}/v1/account_memo.json"
        v1_agent_path = f"{account_path}/v1/retell_agent_spec.json"
        
        if os.path.exists(v1_memo_path):
            try:
                memo = load_json(v1_memo_path)
                data["v1"] = { # type: ignore
                    "exists": True,
                    "company_name": memo.get("company_name", "Unknown"),
                    "services": memo.get("services_supported", []),
                    "business_hours": memo.get("business_hours", {})
                }
            except:
                data["v1"] = {"exists": True, "error": True} # type: ignore
        else:
            data["v1"] = {"exists": False} # type: ignore
        
        # Check v2
        v2_memo_path = f"{account_path}/v2/account_memo.json"
        v2_agent_path = f"{account_path}/v2/retell_agent_spec.json"
        changelog_path = f"{account_path}/v2/changelog_v2.json"
        
        if os.path.exists(v2_memo_path):
            try:
                memo = load_json(v2_memo_path)
                data["v2"] = { # type: ignore
                    "exists": True,
                    "company_name": memo.get("company_name", "Unknown"),
                    "services": memo.get("services_supported", []),
                }
                if os.path.exists(changelog_path):
                    try:
                        changelog = load_json(changelog_path)
                        data["v2"]["changes"] = changelog.get("changes", [])
                    except:
                        pass
            except:
                data["v2"] = {"exists": True, "error": True} # type: ignore
        else:
            data["v2"] = {"exists": False} # type: ignore
        
        accounts.append(data)
    
    return accounts

def get_tasks():
    """Get task data."""
    if os.path.exists(TASKS_FILE):
        return load_json(TASKS_FILE)
    return {"tasks": [], "summary": {"total": 0, "completed": 0}}

def generate_dashboard():
    """Generate HTML dashboard."""
    accounts = get_account_data()
    tasks_data = get_tasks()
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Clara Answers Pipeline Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f7fa; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #2c3e50; margin-bottom: 10px; }}
        .subtitle {{ color: #7f8c8d; margin-bottom: 30px; }}
        
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .stat-card h3 {{ color: #7f8c8d; font-size: 14px; text-transform: uppercase; margin-bottom: 10px; }}
        .stat-card .value {{ font-size: 32px; font-weight: bold; color: #2c3e50; }}
        .stat-card .value.success {{ color: #27ae60; }}
        .stat-card .value.warning {{ color: #f39c12; }}
        
        .section {{ background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }}
        .section h2 {{ color: #2c3e50; margin-bottom: 20px; font-size: 20px; }}
        
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ecf0f1; }}
        th {{ background: #f8f9fa; color: #7f8c8d; font-weight: 600; font-size: 12px; text-transform: uppercase; }}
        
        .status {{ display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }}
        .status.v1 {{ background: #e8f5e9; color: #27ae60; }}
        .status.v2 {{ background: #e3f2fd; color: #2196f3; }}
        .status.missing {{ background: #ffebee; color: #e74c3c; }}
        
        .services {{ display: flex; flex-wrap: wrap; gap: 5px; }}
        .service-tag {{ background: #f0f0f0; padding: 3px 8px; border-radius: 4px; font-size: 11px; color: #555; }}
        
        .change {{ background: #fff8e1; padding: 8px; border-radius: 4px; margin: 5px 0; font-size: 12px; }}
        
        .refresh {{ position: fixed; top: 20px; right: 20px; background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }}
        .refresh:hover {{ background: #2980b9; }}
        
        .footer {{ text-align: center; color: #7f8c8d; margin-top: 30px; font-size: 12px; }}
    </style>
</head>
<body>
    <button class="refresh" onclick="location.reload()">Refresh</button>
    
    <div class="container">
        <h1>🤖 Clara Answers Pipeline Dashboard</h1>
        <p class="subtitle">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="stats">
            <div class="stat-card">
                <h3>Total Accounts</h3>
                <div class="value">{len(accounts)}</div>
            </div>
            <div class="stat-card">
                <h3>v1 Configured</h3>
                <div class="value success">{sum(1 for a in accounts if a.get('v1', {}).get('exists'))}</div>
            </div>
            <div class="stat-card">
                <h3>v2 Configured</h3>
                <div class="value success">{sum(1 for a in accounts if a.get('v2', {}).get('exists'))}</div>
            </div>
            <div class="stat-card">
                <h3>Tasks Completed</h3>
                <div class="value">{tasks_data.get('summary', {}).get('completed', 0)}/{tasks_data.get('summary', {}).get('total', 0)}</div>
            </div>
        </div>
        
        <div class="section">
            <h2>📋 Account Overview</h2>
            <table>
                <thead>
                    <tr>
                        <th>Account ID</th>
                        <th>Company</th>
                        <th>Services</th>
                        <th>v1 Status</th>
                        <th>v2 Status</th>
                    </tr>
                </thead>
                <tbody>
"""
    
    for account in accounts:
        company = account.get("v1", {}).get("company_name") or account.get("v2", {}).get("company_name") or "Unknown"
        
        v1_services = account.get("v1", {}).get("services", [])
        v2_services = account.get("v2", {}).get("services", [])
        
        v1_status = '<span class="status v1">✓ Configured</span>' if account.get("v1", {}).get("exists") else '<span class="status missing">✗ Missing</span>'
        v2_status = '<span class="status v2">✓ Configured</span>' if account.get("v2", {}).get("exists") else '<span class="status missing">✗ Missing</span>'
        
        services_html = '<div class="services">' + ''.join([f'<span class="service-tag">{s}</span>' for s in (v2_services or v1_services)]) + '</div>'
        
        html += f"""
                    <tr>
                        <td><strong>{account['account_id']}</strong></td>
                        <td>{company}</td>
                        <td>{services_html}</td>
                        <td>{v1_status}</td>
                        <td>{v2_status}</td>
                    </tr>
"""
    
    html += """
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>📝 Recent Changes (v1 → v2)</h2>
"""
    
    for account in accounts:
        changes = account.get("v2", {}).get("changes", [])
        if changes:
            html += f"""
            <div style="margin-bottom: 20px;">
                <strong>{account['account_id']}</strong>
"""
            for change in changes:
                html += f"""
                <div class="change">• {change.get('description', 'Updated')} ({change.get('field', 'N/A')})</div>
"""
            html += """
            </div>
"""
    
    html += """
        </div>
        
        <div class="footer">
            Clara Answers Pipeline | Zero-Cost Automation
        </div>
    </div>
</body>
</html>
"""
    
    # Save dashboard
    dashboard_path = f"{BASE_DIR}/outputs/dashboard.html"
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Dashboard generated: {dashboard_path}")
    return dashboard_path

if __name__ == "__main__":
    path = generate_dashboard()
    print(f"\nOpen this file in your browser: {path}")

