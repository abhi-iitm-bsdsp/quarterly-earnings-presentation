# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 23:11:48 2025

@author: Abhishek Seth
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data
# Example: Customer engagement across weekdays and hours
np.random.seed(42)
hours = [f"{h}:00" for h in range(8, 20)]  # 8 AM to 7 PM
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data = np.random.randint(20, 100, size=(len(weekdays), len(hours)))
df = pd.DataFrame(data, index=weekdays, columns=hours)

# Create 512x512 figure (8 inches * 64 dpi = 512 px)
plt.figure(figsize=(8, 8))

# Heatmap
sns.heatmap(df, cmap="Blues", annot=False, linewidths=0.5)

plt.title("Customer Engagement Heatmap")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")

# Save the chart (EXACT 512x512)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
