import sys
from collections import deque

sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())
stack = deque()

for i in range(n):
    temp = int(input())
    print(stack)
    if len(stack) == 0 :
        stack.append(temp)
    else:
        if stack[-1] <= temp :
            for j in range(len(stack)):
                if stack[len(stack)-1] <= temp:   #처음에 j를 넣어서..
                    stack.pop()
                else:
                    break
                    
            stack.append(temp)
        else:
            stack.append(temp)
print(stack)
print(len(stack))