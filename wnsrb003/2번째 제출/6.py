# 사냥꾼 
# https://www.acmicpc.net/problem/8983
# 이분탐색

import sys

사대수, 동물수, 사정거리 = list(map(int, sys.stdin.readline().strip().split()))
사대 = list(map(int, sys.stdin.readline().strip().split()))
사대.sort()
동물 = []
for i in range(동물수):
    동물.append(((list(map(int,sys.stdin.readline().strip().split())))))
# 동물 = [(7,2), (3,3), (4,5), (5,1), (2,2), (1,4), (8,4), (9,4)]
def 찾기(x, start, end):
    while start < end:
        mid = (start+end)//2
        if 사대[mid] == x:
            return x
        else :
            if 사대[mid] < x :
                start = mid + 1
            else :
                end = mid - 1
    if mid == len(사대)-1:
        if abs(사대[mid] - x) >= abs(사대[mid-1] - x): 
            return 사대[mid-1]
    elif mid == 0:
        if abs(사대[mid] - x) >= abs(사대[mid+1] - x):
            return 사대[mid+1]
    else :
        if abs(사대[mid] - x) > abs(사대[mid-1] - x) >= abs(사대[mid+1] - x):
            return 사대[mid+1]
        elif abs(사대[mid] - x) > abs(사대[mid+1] - x) >= abs(사대[mid-1] - x):
            return 사대[mid-1]
    return 사대[mid]

cnt = 0
for i in 동물:
    가까운사대 = 찾기(i[0], 0, len(사대))
    if ((가까운사대 - i[0])**2 + i[1]**2) <= 사정거리**2:
        cnt+=1
print(cnt)