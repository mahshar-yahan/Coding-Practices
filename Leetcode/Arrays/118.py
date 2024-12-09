n = 5
# out = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# print(out[4])
test = [[1],[1,1]]
for i in range(5):
    print("i print =",i)
    if i >=2 :
        col = test[i-1]
        for j in range(i+1):
            
# print(test)