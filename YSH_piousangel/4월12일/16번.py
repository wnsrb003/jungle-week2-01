import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

score_board = ['(', '[']

str_list = list(input())
# print(str_list)
stack = []
score = 0
flag = True
for i in range(len(str_list)):
    temp_score = 0
    print(stack)
    print(score)
    if len(stack) == 0 and str_list[i] in score_board:

        stack_cnt = 0
        stack.append(str_list[i])
        
    elif len(stack) == 0 and str_list[i] not in score_board:
        print(str_list[i])
        flag = False
        break

    elif str_list[i] != stack[-1] and str_list[i] == ')' or str_list[i] == ']':
        if stack[-1] == score_board[0] and str_list[i] == ')':
            if len(stack) == 1:
                if stack_cnt == 0:
                    temp_score += 2
                stack.pop()
            else:
                temp_score += 2
                stack_cnt += 1
                temp_list = []
                ohmygod = 0
                while len(stack) > 1 :
                    if ohmygod == 0:
                        stack.pop()
                        temp_score *= 2
                    if ohmygod != 0:
                        temp_list.append(stack.pop())
                    ohmygod = 1
                    if stack[-1] == '(' and ohmygod == 0:
                        temp_score *= 2
                    elif stack[-1] == '[' and ohmygod == 0:
                        temp_score *=3
            for i in range(len(temp_list)):
                stack.append(temp_list[len(temp_list)-1 -i])
            score += temp_score
            
        elif stack[-1] == score_board[1] and str_list[i] == ']':
            if len(stack) == 1:
                if stack_cnt == 0:
                    temp_score += 3
                stack.pop()
            else:
                stack_cnt += 1
                temp_score = 3
                temp_list = []
                ohmygod = 0
                while len(stack) > 1 :
                    if ohmygod == 0:
                        stack.pop()
                        temp_score *= 3
                    if ohmygod != 0:
                        temp_list.append(stack.pop())
                    ohmygod = 1
                    if stack[-1] == '(' and ohmygod == 0 :
                        temp_score *= 2
                    elif stack[-1] == '[' and ohmygod == 0 :
                        temp_score *= 3
            for i in range(len(temp_list)):
                stack.append(temp_list[len(temp_list)-1 -i])
            score += temp_score

    else:
        if stack[-1] == score_board[0] :         
            stack.append(str_list[i])
        elif stack[-1] == score_board[1] :
            stack.append(str_list[i])

print(stack, flag)
if len(stack) != 0 or flag == False:
    print("0")
else:
    print(score)

