import pandas as pd

# Input DataFrame
data = {
    "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas", "Piper"],
    "salary": [4548, 28150, 1103, 6593, 74576, 24433, 4548]
}

employees = pd.DataFrame(data)

employees = employees['salary']*2
print(employees)