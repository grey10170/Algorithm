import sys
rl = sys.stdin.readline
n_case = int(rl())

def countCovering(board, h, w):
    remain = False
    for i, row in enumerate(board):
        if False in row:
            remain = True
            j = row.index(False)
            break
    if not remain:
        return 1
    cnt = 0
    #ㄱ
    if j+1 < w and i+1 <h and not board[i][j+1] and not board[i+1][j+1]:
        board[i][j] = board[i][j+1] = board[i+1][j+1] = True
        cnt += countCovering(board, h, w)
        board[i][j] = board[i][j+1] = board[i+1][j+1] = False
    #ㄱ 세로축 대칭
    if j+1 < w and i+1 <h and not board[i][j+1] and not board[i+1][j]:
        board[i][j] = board[i][j+1] = board[i+1][j] = True
        cnt += countCovering(board, h, w)
        board[i][j] = board[i][j+1] = board[i+1][j] = False
    #ㄴ
    if j+1 < w and i+1 <h and not board[i+1][j] and not board[i+1][j+1]:
        board[i][j] = board[i+1][j+1] = board[i+1][j] = True
        cnt += countCovering(board, h, w)
        board[i][j] = board[i+1][j+1] = board[i+1][j] = False
    #ㄴ 세로축 대칭
    if j > 0 and i+1 <h and not board[i+1][j] and not board[i+1][j-1]:
        board[i][j] = board[i+1][j-1] = board[i+1][j] = True
        cnt += countCovering(board, h, w)
        board[i][j] = board[i+1][j-1] = board[i+1][j] = False
    return cnt
def bitmap2board(bitmap):
    board_string=""
    for row in bitmap:
        for item in row:
            board_string +="#" if item else "."
        board_string += "\n"
    return board_string
for _ in range(n_case):
    h, w = map(int, rl().split())
    board = []
    for _ in range(h):
        x = rl().strip()
        board.append([False if i=="." else True for i in x])
    print(countCovering(board, h, w))