def AddBoard(board, ans):
    temp = []
    print('Add Borad called')
    for i in range(n):
        lis = []
        for j in range(n):
            lis.append(board[i][j])
        temp.append(lis)
    ans.append(temp)

def PlaceQueen(board, isRowOcc, ans, UDiag, LDiag, n, col):
    if col == n:
        AddBoard(board, ans)
        return
    
    for row in range(n):
        # print('Place Queen called')
        if(UDiag[row-col+n-1] == False and LDiag[row+col] == False and isRowOcc[row] == False):
            board[row][col] = 'Q'
            UDiag[row-col+n-1] = LDiag[row+col] = isRowOcc[row] = True
            PlaceQueen(board, isRowOcc, ans, UDiag, LDiag, n, col+1)
            board[row][col] = '.'
            UDiag[row-col+n-1] = LDiag[row+col] = isRowOcc[row] = False

n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
ans = []
isRowOcc = [False] * n
UDiag = [False] * ((2*n)-1)
LDiag = [False] * ((2*n)-1)
col = 0

PlaceQueen(board, isRowOcc, ans, UDiag, LDiag, n, col)
for i in ans:
    for j in i:
        print(j)
    print()