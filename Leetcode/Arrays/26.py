nums = [0,0,1,1,1,2,2,3,3,4]

num_list = []
t = 0
for i in nums:
    if i not in num_list:
        t+=1
        num_list.append(i)

print(t)