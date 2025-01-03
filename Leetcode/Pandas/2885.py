import pandas as pd

# Example DataFrame
data = {
    "id": [1, 2, 3],
    "first": ["Alice", "Bob", "Charlie"],
    "last": ["Smith", "Johnson", "Brown"],
    "age": [20, 21, 22]
}

students = pd.DataFrame(data)

students_renamed = students.rename(
    columns={
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    }
)

print(students_renamed)