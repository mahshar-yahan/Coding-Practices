import pandas as pd
student_data =[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

df = pd.DataFrame(student_data, columns=['student_id ','age'])
l = []
l.append(len(df))
l.append(len(df.columns))
print(l)