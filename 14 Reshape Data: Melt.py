# Reshape Data: Melt
# 
# DataFrame report
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | product     | object |
# | quarter_1   | int    |
# | quarter_2   | int    |
# | quarter_3   | int    |
# | quarter_4   | int    |
# +-------------+--------+
# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

# The result format is in the following example.

 

# Example 1:

# Input:
# +-------------+-----------+-----------+-----------+-----------+
# | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
# +-------------+-----------+-----------+-----------+-----------+
# | Umbrella    | 417       | 224       | 379       | 611       |
# | SleepingBag | 800       | 936       | 93        | 875       |
# +-------------+-----------+-----------+-----------+-----------+
# Output:
# +-------------+-----------+-------+
# | product     | quarter   | sales |
# +-------------+-----------+-------+
# | Umbrella    | quarter_1 | 417   |
# | SleepingBag | quarter_1 | 800   |
# | Umbrella    | quarter_2 | 224   |
# | SleepingBag | quarter_2 | 936   |
# | Umbrella    | quarter_3 | 379   |
# | SleepingBag | quarter_3 | 93    |
# | Umbrella    | quarter_4 | 611   |
# | SleepingBag | quarter_4 | 875   |
# +-------------+-----------+-------+
# Explanation:
# The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    melted = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return melted

report = pd.DataFrame({
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
})

meltTable(report)
## Author: Hemant Thapa
## Date: 11.02.2024
## Challenge: Leet Code 
