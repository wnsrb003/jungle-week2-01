# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

# stack_operation = ['pop', 'size', 'empty', 'top']

sample_stack = []

for i in range(n):
    inputStr = input().split()
    # print(inputStr)
    if len(inputStr) == 2:
        sample_stack.append(inputStr[1])
    else:
        if inputStr[0] ==  'pop':      #stack_operation[0]
            if len(sample_stack) == 0 :
                print("-1")
            else:
                print(sample_stack[-1])
                sample_stack.pop()
        elif inputStr[0] == 'size' :   # stack_operation[1]
            print(len(sample_stack))
        elif inputStr[0] == 'empty' :  # stack_operation[2]
            if not sample_stack :
                print("1")
            else:
                print("0")
        elif inputStr[0] == 'top':        # stack_operation[3]
            if not sample_stack :
                print("-1")
            else:
                print(sample_stack[-1])


