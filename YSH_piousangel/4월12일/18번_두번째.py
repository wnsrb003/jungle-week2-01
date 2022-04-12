import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline
N, K = map(int, input().split())

num_str = input()
stack = []
cnt = 0

for i in range(len(num_str)):
    now_num = num_str[i]
   
    if len(stack) == 0:
        stack.append([now_num,i])
    elif len(stack) < K :           #큰수가 stack[-1]로 오게 만들어줍니다.
        if stack[-1][0] < now_num :        
            stack.append([now_num,i])    
        else:
            temp_box = []
            while len(stack) > 0 :
                if stack[-1][0] <= now_num :
                     stack.append([now_num,i])
                     break
                if len(stack) == 1 and stack[-1][0] > now_num:
                    callback = stack.pop()
                    temp_box.append(callback)
                    stack.append([now_num,i])
                    break
                else:
                    callback = stack.pop()
                    temp_box.append(callback)
            idx = 0
            for i in range(len(temp_box)):
                stack.append(temp_box[len(temp_box)-1-i])

    else:                 #스택수가 K개 일때 부터
        if stack[-1][0] <= now_num :
            continue
        else:
            temp_box = []
            # print("============",i)
            while len(stack) > 0 :
                if stack[-1][0] <= now_num :
                     stack.append([now_num,i])
                     break
                callback = stack.pop()
                temp_box.append(callback)
            # print("temp_box", temp_box)
            idx = 0
            while len(stack) < K :
                stack.append(temp_box[len(temp_box)-1-idx])
                idx += 1

 
print("stack", stack)
 
answer_str = ""
print("num_str", num_str)
for i in range(len(num_str)):
    flag = True
    for j in range(len(stack)):

        if i == stack[j][1]:
            print("stack[j][1]",stack[j][1])
            flag = False
            break
    if flag:
        print("i", i)
        answer_str += num_str[i]

print(answer_str)
