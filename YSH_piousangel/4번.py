n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()
left_idx = 0
right_idx = len(n_list)-1

answer = [0,0]
tmp_answer = 10000000000001
# flag = True

while right_idx > left_idx :

    left_value = n_list[left_idx]
    right_value = n_list[right_idx]

    if abs(right_value+ left_value) == 0 :
        answer[0] = left_value
        answer[1] = right_value
        break

    if tmp_answer > abs(right_value + left_value):
        answer[0] = left_value
        answer[1] = right_value
        tmp_answer = abs(right_value + left_value)

    if right_value + left_value < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(answer[0], answer[1])