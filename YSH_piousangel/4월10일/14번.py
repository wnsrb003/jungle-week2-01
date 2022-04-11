from collections import deque
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

def chkCorrect(temp_str, stack):
    
    if temp_str[0] == ')' :
        return False
    for idx in range(len(temp_str)):
        
        if len(stack) == 0 :
            if temp_str[idx] == '(':
                stack.append(temp_str[idx])
            else :   
                return False
        else :
            if stack[-1] == '(' and temp_str[idx] == ')':
                stack.pop()
            else:
                stack.append(temp_str[idx])
    # print(stack)
    if len(stack) == 0 :
        return True
    else:
        return False
    

for i in range(n):
    temp_str = input().rstrip()
    stack = deque()

    if chkCorrect(temp_str, stack) :
        print("YES")
    else:
        print("NO")
        
    


