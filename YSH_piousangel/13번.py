n = int(input())

stack_A = []
for i in range(n):
    temp = int(input())

    if temp == 0:
        stack_A.pop()
    else:
        stack_A.append(temp)

print(sum(stack_A))