row_index = 1
# out = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# print(out[4])
temp1 = [[1]]
test = [[1],[1,1]]
for i in range(row_index+1):
    if i >=2 :
        col = test[i-1]
        temp = []
        for j in range(i+1):
            if j ==0: 
                temp.append(1)
            elif j==len(col):
                temp.append(1)
            else:
                temp.append(col[j-1]+col[j])
        test.append(temp)
if (row_index) == 0:
    print(temp1)
else:    
    print((test))
    print(test[len(test)-1])