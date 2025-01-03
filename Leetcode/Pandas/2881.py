import pandas as pd


data = {
    "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
    "salary": [4548, 28150, 1103, 6593, 74576, 24433]
}

employees = pd.DataFrame(data)

employees['bonus'] = employees['salary']*2

print(employees)
