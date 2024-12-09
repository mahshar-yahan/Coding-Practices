prices = [1,2,10,40]
profit = 0
buy = prices[0]
for i in range(1,len(prices)):
    if prices[i] < buy:
        buy = prices[i]
    elif prices[i] - buy >profit:
        profit = prices[i] - buy
print(profit)