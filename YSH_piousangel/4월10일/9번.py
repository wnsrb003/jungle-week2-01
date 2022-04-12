import sys
input = sys.stdin.readline

N, B = map(int,input().split())

box = []
for i in range(N):
    box.append(list(map(int, input().split())))
# answer = [[0 for i in range(len(box))] for _ in range(len(box))]

def calculator(arr, arr2):

    temp_arr = [[0 for i in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)) :
        for j in range(len(arr)):
            for k in range(len(arr)):
                temp_arr[i][j] += (arr[i][k] * arr2[k][j])
            
            temp_arr[i][j] %= 1000
    return temp_arr

def dfs(box, B) :

    if B == 1 :
        for i in range(len(box)):
            for j in range(len(box[0])):
                box[i][j] %= 1000
        return box

    bar = dfs(box, B//2)

    if B % 2 != 0 :
        return calculator(calculator(bar, bar), box)
    else:
        return calculator(bar, bar) 

kk = dfs(box, B)

for i in kk:
    print(*i)