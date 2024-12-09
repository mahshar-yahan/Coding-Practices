digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
res = []
d_c = ''
for i in digits:
    d_c = d_c + str(i)
d_f = str(int(d_c)+1)
for i in d_f:
    res.append(i)
print(res)

