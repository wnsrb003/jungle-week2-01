#철로
#https://www.acmicpc.net/problem/13334
#우선순위큐
import sys
import heapq

# n = 8
# 철로 = [[5,40], [25,35], [10,20], [10,25], [30,50], [50,60], [25,30], [80,100]]
# d = 30

n = int(sys.stdin.readline().strip())
철로 = []
for i in range(n) : 
    x = list(map(int, sys.stdin.readline().strip().split()))
    if x[1]<x[0]:
        x = [x[1], x[0]]
    철로.append(x)
d = int(sys.stdin.readline().strip())

배열 = []
큐 = []
최대 = 0
# 출퇴근 = 철로.pop()
#heapq.heappop(배열)
while 철로:
    출퇴근 = 철로.pop(0)
    if not 배열:
        if 출퇴근[1] - 출퇴근[0] <= d:
            # heapq.heappush(배열, [0, 출퇴근[0], 출퇴근[0]+d])
            # 배열.append([0, 출퇴근[0], 출퇴근[0]+d])
            # 배열.append([0, 출퇴근[1]-d, 출퇴근[1]])
            # heapq.heappush(배열, [0, 출퇴근[1]-d, 출퇴근[1]])
            
        # else :
            heapq.heappush(배열, [1, 출퇴근[0], 출퇴근[0]+d])
            # 배열.append([1, 출퇴근[0], 출퇴근[0]+d])
            # 배열.append([1, 출퇴근[1]-d, 출퇴근[1]])
            heapq.heappush(배열, [1, 출퇴근[1]-d, 출퇴근[1]])
    else :
        flag = 0
        뺀놈들 = []
        for _ in range(len(배열)) :
            뺀놈 = heapq.heappop(배열)
            if 뺀놈[1] <= 출퇴근[0] and 뺀놈[2] >= 출퇴근[1]:
                heapq.heappush(배열, [뺀놈[0]+1, 뺀놈[1], 뺀놈[2]])
                flag += 1
            else :
                뺀놈들.append(뺀놈)
        if not flag :
            if 출퇴근[1] - 출퇴근[0] <= d:
                # heapq.heappush(배열, [0, 출퇴근[0], 출퇴근[0]+d])
                # heapq.heappush(배열, [0, 출퇴근[1]-d, 출퇴근[1]])
                # break
            # else :
                heapq.heappush(배열, [1, 출퇴근[0], 출퇴근[0]+d])
                heapq.heappush(배열, [1, 출퇴근[1]-d, 출퇴근[1]])
        for i in 뺀놈들:
            heapq.heappush(배열, i)
        
if 배열 : 
    print(max([i[0] for i in 배열]))
else :
    print(0)

                


