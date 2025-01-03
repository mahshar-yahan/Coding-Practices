import pandas as pd

# Example DataFrame
data = {
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 22],
    "grade": [85.5, 90.0, 78.2]
}

students = pd.DataFrame(data)

# Convert the 'grade' column to integers
students["grade"] = students["grade"].astype(int)
print(students)