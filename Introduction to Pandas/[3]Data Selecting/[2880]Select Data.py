# 
# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# 
#  
# 
#  Write a solution to select the name and age of the student with student_id = 
# 101. 
# 
#  The result format is in the following example. 
# 
#  
#  
# Example 1:
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Output:
# +---------+-----+
# | name    | age | 
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# Explanation:
# Student Ulysses has student_id = 101, we select the name and age. 
# 
#  👍 74 👎 6

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]


# test from here
students = pd.DataFrame({
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
})
print(selectData(students))
