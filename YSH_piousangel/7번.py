import sys                                   #프로그래머스의 쿼드압축후 더하기 문제와 동일한 문제네요!
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
answer = [0,0]

def chkPaper(board, lenOfBoard, row_s, col_s):
    global answer
    for i in range(row_s, row_s+lenOfBoard):
        for j in range(col_s, col_s+lenOfBoard):
            if board[i][j] != board[row_s][col_s] :
                return False
            
    answer[board[row_s][col_s]] += 1
    return True

def dfs(board, lenOfBoard, row_s, col_s) :
    global answer
    if lenOfBoard == 1:
        answer[board[row_s][col_s]] += 1
        return

    if chkPaper(board, lenOfBoard, row_s, col_s) :
        return
    
    dfs(board, lenOfBoard//2, row_s, col_s)
    dfs(board, lenOfBoard//2, row_s+lenOfBoard//2, col_s)
    dfs(board, lenOfBoard//2, row_s, col_s+lenOfBoard//2)
    dfs(board, lenOfBoard//2, row_s+lenOfBoard//2, col_s+lenOfBoard//2)

dfs(board, n, 0, 0)
print(answer[0])
print(answer[1])