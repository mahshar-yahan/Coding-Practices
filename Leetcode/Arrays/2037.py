seats = [2,2,6,6]
students = [1,3,2,6]
seats = sorted(seats)
students = sorted(students)
res = 0
for i in range(len(seats)):
    t = seats[i]-students[i]
    res = (res+t) if t>=0 else (res-t)

print(res)