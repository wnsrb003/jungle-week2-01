import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, C = map(int, input().split())

n_list = []

for i in range(N):
    n_list.append(int(input()))

n_list.sort()

left_idx = 0
right_idx = len(n_list) - 1

wifi_list = []
wifi_list.append(left_idx)
wifi_list.append(right_idx)


def dfs(n_list, wifi_list, C, left_idx, right_idx) :                 #짝수일 때 에러발생

    # if len(wifi_list) == C :
    #     return

    if C == 1:
        return

    if right_idx <= left_idx :
        return

    mid_idx = (right_idx+left_idx) // 2

    wifi_list.append(mid_idx)

    # if flag:
    #     flag = False
    dfs(n_list, wifi_list, C//2, mid_idx+1, right_idx)
    # else:
    #     flag = True
    dfs(n_list, wifi_list, C//2, left_idx, mid_idx-1)
    

dfs(n_list, wifi_list, C-2, left_idx, right_idx)

minValue = 10000000001
wifi_list.sort()
print(wifi_list)
for i in range(len(wifi_list)-1):
    minValue = min(abs(n_list[wifi_list[i]]- n_list[wifi_list[i+1]]), minValue)

print(minValue)

