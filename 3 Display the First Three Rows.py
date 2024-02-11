# Display the First Three Rows

# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.

 

# Example 1:

# Input:
# DataFrame employees
# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  |
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+
# Output:
# +-------------+---------+-------------+--------+
# | employee_id | name    | department  | salary |
# +-------------+---------+-------------+--------+
# | 3           | Bob     | Operations  | 48675  |
# | 90          | Alice   | Sales       | 11096  |
# | 9           | Tatiana | Engineering | 33805  |
# +-------------+---------+-------------+--------+
# Explanation: 
# Only the first 3 rows are displayed.

import pandas as pd

employees = [
    {"employee_id": 3, "name": "Bob", "department": "Operations", "salary": 48675},
    {"employee_id": 90, "name": "Alice", "department": "Sales", "salary": 11096},
    {"employee_id": 9, "name": "Tatiana", "department": "Engineering", "salary": 33805},
    {"employee_id": 60, "name": "Annabelle", "department": "InformationTechnology", "salary": 37678},
    {"employee_id": 49, "name": "Jonathan", "department": "HumanResources", "salary": 23793},
    {"employee_id": 43, "name": "Khaled", "department": "Administration", "salary": 40454}
]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)
    return df[0:3]

selectFirstRows(employees)

## Author: Hemant Thapa
## Date: 11.02.2024
## Challenge: Leet Code 
