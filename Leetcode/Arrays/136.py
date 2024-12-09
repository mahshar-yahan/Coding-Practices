nums = [2,2,1]
test = {}
for i in nums:
    if i not in test:
        test[i] = 1
    else:
        test[i] += 1
for num, count in test.items():
    if count == 1:
        print(num)
        break