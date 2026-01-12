from datetime import datetime

# 1. Our Data Structure: A List of Dictionaries
# Each dictionary represents a single Insurance Claim
claims = [
    {"patient": "John Doe", "amount": 450.00, "date_sent": "2025-12-15"},
    {"patient": "Jane Smith", "amount": 1200.00, "date_sent": "2026-01-05"},
    {"patient": "Alice Brown", "amount": 85.00, "date_sent": "2025-11-20"},
    {"patient": "Bob Wilson", "amount": 300.00, "date_sent": "2025-10-01"},
]

def run_aging_report(claim_list):
    today = datetime.now()
    
    # 2. Our Aging Buckets (Categories)
    buckets = {
        "Current (0-30 days)": 0,
        "Overdue (31-60 days)": 0,
        "Late (61-90 days)": 0,
        "Collection (90+ days)": 0
    }

    print(f"--- DENTRIX MOCK AGING REPORT ({today.strftime('%Y-%m-%d')}) ---")
    
    for claim in claim_list:
        # Convert the string date to a Python date object
        date_obj = datetime.strptime(claim["date_sent"], "%Y-%m-%d")
        
        # Calculate the difference in days
        days_old = (today - date_obj).days
        
        # 3. Logic to sort into the correct Dictionary Key
        if days_old <= 30:
            buckets["Current (0-30 days)"] += claim["amount"]
        elif days_old <= 60:
            buckets["Overdue (31-60 days)"] += claim["amount"]
        elif days_old <= 90:
            buckets["Late (61-90 days)"] += claim["amount"]
        else:
            buckets["Collection (90+ days)"] += claim["amount"]
            
    # 4. Display the Results
    for category, total in buckets.items():
        print(f"{category}: ${total:,.2f}")

run_aging_report(claims)