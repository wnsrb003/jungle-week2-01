import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, B = map(int,input().split())

box = []
for i in range(N):
    box.append(list(map(int, input().split())))

def calculator(arr, arr2):

    temp_arr = [[0 for i in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)) :
        for j in range(len(arr)):
            for k in range(len(arr)):
                temp_arr[i][j] += arr[i][k] * arr[k][j]
            temp_arr[i][j] %= 1000
    return temp_arr

def dfs(box, B) :

    if B == 1 :
        for i in range(len(box)):
            for j in range(len(box[0])):
                box[i][j] %= 1000
        return box

    pair = dfs(box, B//2)

    if B % 2 != 0 :
        return calculator(calculator(pair, pair), box)
    else:
        return calculator(pair, pair) 

answer = dfs(box, B)

for i in answer :
    print(i , end =" ")
    print()