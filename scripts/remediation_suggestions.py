#!/usr/bin/env python3
import pandas as pd
from datetime import datetime

df = pd.read_csv("data/historical_compliance.csv")

print("\n🔍 Corrective Action Report")
print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 80)

for _, row in df.iterrows():
    if row["score"] < 70:
        print(f"\n⚠️ Control: {row['control_name']} ({row['framework']})")
        print(f"   Asset Class: {row['asset_class']}")
        print(f"   Current Score: {row['score']}%")
        print(f"   Last Audit: {row['last_audit']}")
        print("   Recommended Action:")

        if row["asset_class"] == "Endpoint Security":
            print("   → Apply critical OS patches and verify endpoint EDR coverage.")
        elif row["asset_class"] == "Infrastructure Security":
            print("   → Review vulnerability scans and validate firewall ACLs.")
        elif row["asset_class"] == "Data Governance":
            print("   → Update retention schedules and revalidate consent management.")
        else:
            print("   → Conduct control reassessment and apply updated baselines.")

print("\n✅ Corrective action review complete.\n")
