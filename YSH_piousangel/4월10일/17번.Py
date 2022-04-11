from collections import deque
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

tower_list = list(map(int, input().split()))
answer = []
stack = deque()
idx = 0
for i in range(len(tower_list)):
    if i == 0 :
        answer.append(0)
        stack.append([tower_list[i], i+1])

    else:
        if stack[-1][0] >= tower_list[i] :
            answer.append(stack[-1][1])
            stack.append([tower_list[i], i+1])
        else:
            flag = True
            while stack[-1][0] < tower_list[i] :
                stack.pop()
                if len(stack) == 0:
                    answer.append(0)
                    flag = False
                    break
            if flag:
                answer.append(stack[-1][1])
            stack.append([tower_list[i],i+1])

print(stack)
            
for k in answer :
    print(k, end=" ")
    


