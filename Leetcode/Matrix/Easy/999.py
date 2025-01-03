board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]



for i in range(8):
    for j in range(8):
        if board[i][j] =="R":
            row = i
            col = j
            break
output = 0
#lower
for i in range(row+1,8):
    if board[i][col]=="p":
        output +=1
    elif board[i][col]!=".":
        break
#upper
for i in range(0,row):
    if board[i][col]=="p":
        output +=1
    elif board[i][col]!=".":
        break
#right
for i in range(col+1,8):
    if board[row][i]=="p":
        output +=1
    elif board[row][i]!=".":
        break
#left
for i in range(0,col):
    # print(f"{board[row][i]}\n")
    if board[row][i]=="p":
        output +=1
    elif board[row][i]!=".":
        break


print(row, col,output)