# Create a New Column

# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.

# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

# The result format is in the following example.

 

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+
# Output:
# +---------+--------+--------+
# | name    | salary | bonus  |
# +---------+--------+--------+
# | Piper   | 4548   | 9096   |
# | Grace   | 28150  | 56300  |
# | Georgia | 1103   | 2206   |
# | Willow  | 6593   | 13186  |
# | Finn    | 74576  | 149152 |
# | Thomas  | 24433  | 48866  |
# +---------+--------+--------+
# Explanation: 
# A new column bonus is created by doubling the value in the column salary.


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(employees)
        df['bonus'] = df['salary'] * 2
        return df

employees = [
    {"name": "Piper", "salary": 4548},
    {"name": "Grace", "salary": 28150},
    {"name": "Georgia", "salary": 1103},
    {"name": "Willow", "salary": 6593},
    {"name": "Finn", "salary": 74576},
    {"name": "Thomas", "salary": 24433}
]

createBonusColumn(employees)

## Author: Hemant Thapa
## Date: 11.02.2024
## Challenge: Leet Code 
