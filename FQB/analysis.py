# analysis.py
# Author: 23f1001785@ds.study.iitm.ac.in
# Business Case: Retail Performance Analysis

import matplotlib.pyplot as plt

# Quarterly Inventory Turnover Ratio Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_ratio = [3.34, 2.3, 10.01, 11.87]
industry_target = 8

# Calculate average
average_turnover = sum(turnover_ratio)/len(turnover_ratio)
print(f"Average Inventory Turnover Ratio: {average_turnover:.2f}")

# Visualization
plt.figure(figsize=(8,5))
plt.plot(quarters, turnover_ratio, marker='o', linestyle='-', color='blue', label='Company')
plt.axhline(y=industry_target, color='red', linestyle='--', label='Industry Target (8)')
plt.title("Inventory Turnover Ratio - Quarterly Performance (2024)\n23f1001785@ds.study.iitm.ac.in")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.ylim(0, max(turnover_ratio)+2)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Save chart
plt.savefig("inventory_turnover.png", dpi=150)
plt.show()
