# -*- coding: utf-8 -*-
"""
This script reads data from a CSV file, creates two pie charts, and displays them in separate subplots.
The data represents agricultural and Forest land percentages for different countries.

Created on Wed Nov  8 06:10:09 2023

@author: Kinza Ijaz

"""
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("/Users/Ammad computer/Documents/Land size.csv")

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# First pie chart
x1 = df["Country"]
y1 = df["Agricultural_land"]
ax1.pie(y1, labels=x1, radius=1.0, autopct="%0.01f%%",
        shadow=True, explode=[0.05, 0.2, 0.05, 0.2, 0.05, 0.2, 0.05],
        colors=["red", "blue", "green", "yellow", "purple", "orange", "pink"])
ax1.set_title('Agricultural land (% of land area)', fontsize=15)

# Second pie chart
x2 = df["Country"]
y2 = df["Forest_land"]
ax2.pie(y2, labels=x2, radius=0.9, autopct="%0.01f%%",
        shadow=True, explode=[0.05, 0.2, 0.05, 0.2, 0.05, 0.2, 0.05],
        colors=["red", "blue", "green", "yellow", "purple", "orange", "pink"])
ax2.set_title('Forest land (% of land area)', fontsize=15)

# Adjust layout
plt.tight_layout()

# Display the pie charts
plt.show()






