import sys                         ##투포인터로 푼다는 것을 검색해서 알았습니다. 하지만 답을 보진 않았습니다!
sys.setrecursionlimit(10**9)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

left_value = n_list[0]
right_value = n_list[-1]

answer = [0,0]

def dfs(n_list, left_idx, right_idx, tmp_answer) :
    global answer

    left_value = n_list[left_idx]
    right_value = n_list[right_idx]

    if abs(left_value + right_value) == 0:
        answer[0] = left_value
        answer[1] = right_value
        return
    
    if right_idx <= left_idx :
        return
    
    if tmp_answer > abs(right_value + left_value):
        answer[0] = left_value
        answer[1] = right_value

    if right_value + left_value < 0:
        dfs(n_list, left_idx+1, right_idx, min(abs(right_value+left_value), tmp_answer))
    else:
        dfs(n_list, left_idx, right_idx-1, min(abs(right_value+left_value), tmp_answer))
    
dfs(n_list, 0, len(n_list)-1, 1000000000001)

print(answer[0], answer[1])

