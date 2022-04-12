import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

number_str = input()

cnt = len(number_str) - K

box = [0] * cnt
visited = [False] * len(number_str)
answer = 0

def chkMaxNum(box):
    global answer
    temp_num = 0
    str_ = ""
    for i in range(len(box)):
        str_ += box[i]
    
    temp_num = int(str_)
    answer = max(answer, temp_num)
    return


def dfs(number_str, box, visited, startIdx, idx):

    if idx == len(box):
        chkMaxNum(box)
        return

    for i in range(startIdx, len(number_str)):
        if visited[i] != True:
            visited[i] = True
            box[idx] = number_str[i]
            dfs(number_str, box, visited, i+1, idx+1)
            visited[i]= False

dfs(number_str, box, visited, 0, 0)
print(answer)