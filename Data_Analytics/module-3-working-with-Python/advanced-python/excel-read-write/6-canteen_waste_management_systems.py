# task 
'''
Task: Visualize Food Wastage in a Canteen Management System

Create a Python program using Pandas and Matplotlib to analyze and visualize food wastage in a canteen management system.

Requirements

Create a dataset containing:

Food item name

Quantity prepared (in kg)

Quantity consumed (in kg)

Quantity wasted (in kg)

Create a Pandas DataFrame from the dataset.

Calculate the total food wastage for each food item.

Use a pie chart to visualize the percentage of total food wastage contributed by each food item.

Display:

Food item names as labels

Wasted quantity as the pie-chart values

Percentage of wastage on each slice

A suitable chart title such as "Canteen Food Wastage Analysis"

Display the DataFrame before displaying the chart.

Expected Output

The program should display a table containing the canteen food-wastage data and a pie chart showing the proportion of total wastage for each food item.

Example Food Items

Rice

Dal

Vegetables

Chapati

Curry

Salad

The objective is to help canteen management identify which food items contribute most to overall food wastage.


'''

import pandas as pd
import matplotlib.pyplot as plt

# Canteen food wastage data
data = {
    "food_item": ["Rice", "Dal", "Vegetables", "Chapati", "Curry", "Salad"],
    "quantity_prepared": [50, 30, 25, 40, 35, 15],
    "quantity_consumed": [42, 25, 20, 35, 28, 10],
    "quantity_wasted": [8, 5, 5, 5, 7, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print("Canteen Food Wastage Data")
print(df)

# Calculate total food wastage
total_wastage = df["quantity_wasted"].sum()

print("\nTotal Food Wastage:", total_wastage, "kg")

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    df["quantity_wasted"],
    labels=df["food_item"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Canteen Food Wastage Analysis")
plt.show()
