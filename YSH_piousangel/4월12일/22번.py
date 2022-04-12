from collections import deque
N, K = map(int, input().split())

round_q = deque()

for i in range(1, N+1):
    round_q.append(i)

cnt = 1
answer_list = []
while round_q :

    temp = round_q.popleft()
    if cnt == K :
        answer_list.append(temp)
        cnt = 0
    else:
        round_q.append(temp)
    
    cnt += 1

for i in range(len(answer_list)):
    if i == 0:
        print('<', end="")
    if i == len(answer_list)-1:
        print(answer_list[i], end="")
        print('>')
    else:
        print(answer_list[i], end=', ')

