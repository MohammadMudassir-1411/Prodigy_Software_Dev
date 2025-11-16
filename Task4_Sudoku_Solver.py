board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def ok(num, r, c):
    for x in range(9):
        if board[r][x] == num:
            return False
    for x in range(9):
        if board[x][c] == num:
            return False
    r1 = (r // 3) * 3
    c1 = (c // 3) * 3
    for rr in range(r1, r1 + 3):
        for cc in range(c1, c1 + 3):
            if board[rr][cc] == num:
                return False
    return True
def solve():
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if ok(num, r, c):
                        board[r][c] = num
                        if solve():
                            return True
                        board[r][c] = 0
                return False
    return True 
solve()
for row in board:
    print(row)