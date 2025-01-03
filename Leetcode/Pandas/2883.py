import pandas as pd

# Example DataFrame
data = {
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Alice", None, "Charlie", "David", None],
    "age": [20, 21, 22, 23, 24]
}

students = pd.DataFrame(data)

temp = students.dropna(subset=['name'])
print(temp)