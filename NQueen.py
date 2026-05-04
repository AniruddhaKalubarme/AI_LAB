def PlaceQueen(board, n, Udiag, Ldiag, col, ans, RowOccurence):
    if(col == n):
        ans.append([r[:] for r in board])
        return
    
    for row in range(0, n):
        if(RowOccurence[row] == -1 and Udiag[n-1+row-col] == -1 and Ldiag[col+row] == -1):
            board[col][row] = 'Q'
            Udiag[n-1+row-col] = Ldiag[col+row] = RowOccurence[row] = 1
            PlaceQueen(board, n, Udiag, Ldiag, col+1, ans, RowOccurence)
            board[col][row] = '.'
            Udiag[n-1+row-col] = Ldiag[col+row] = RowOccurence[row] = -1

               

n = 4
board = [['.' for i in range(0,n)] for j in range(0,n)]
Udiag = [-1] * (2*n - 1)
Ldiag = [-1] * (2*n - 1)
RowOccurence = [-1]*n
ans = []
PlaceQueen(board, n, Udiag, Ldiag, 0, ans, RowOccurence)

for i in ans:
    for j in i:
        print(j)
    print('----------------------')