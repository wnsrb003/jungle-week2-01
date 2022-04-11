import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

while True :

    n_list = list(map(int, input().split()))

    if n_list[0] == 0 :
        break

    num = n_list[0]
    height_list = n_list[1:]
    # print("height_list", height_list)
    stack = deque()
    floor = 1 * len(height_list)
    stack.append(floor)

    upperCnt = 1
    idx = 0
    height = 0
    k = 1
    for i in range(len(height_list)) :
        if upperCnt == 1:
            idx = i
            height = height_list[idx]
            upperCnt += 1                    #막대기 하나 추가하려고 
            
        else:
            if height_list[i] < height_list[i-1] :
                # print("uperCnt", upperCnt, idx)
                area = upperCnt * height
                if area > stack[-1] :
                    stack.pop()
                    stack.append(area)
                    upperCnt = 1
            else:
                if upperCnt * height < k * height_list[idx+1]:       #기존의 밑길이가 * 높이가 큰 높이들이 들어와 넓이 최대가 깨질 때 (여기가 잘 구현이 안된 것 같아요)
                    height = height_list[idx+1]  #밑길이는 그대로 두고, 높이만 변경
                    upperCnt = k   #k일때 넓이가 더 커졌으므로 밑길이는 k로 변경

                else:
                    upperCnt += 1
                    # idx += 1
                    k+= 1

    if (upperCnt-1) * height > stack[-1]:    #높이가 안바뀌고 끝나면 stack 값과 비교해주기
        stack.pop()
        stack.append((upperCnt-1) * height)

    print(stack[-1])
    # print("=====")
