# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

# The result format is in the following example.

 

# Example 1:

# Input:
# student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]
# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1          | 15  |
# | 2          | 11  |
# | 3          | 11  |
# | 4          | 20  |
# +------------+-----+
# Explanation:
# A DataFrame was created on top of student_data, with two columns named student_id and age.

import pandas as pd
from typing import List

def createDataframe(student_data):
    data = {"student_id": [], "age": []}
    for i in student_data:
        data["student_id"].append(i[0])
        data["age"].append(i[1])
    df = pd.DataFrame(data)
    return df

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
createDataframe(student_data)

## Author: Hemant Thapa
## Date: 11.02.2024
## Challenge: Leet Code 
