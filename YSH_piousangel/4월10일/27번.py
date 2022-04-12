import sys
import heapq
import copy
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
rail_heap = []
min_value = 10000001
max_value = -10000001
start_list = []
for i in range(n):
    start, end = map(int, input().split())
    temp = 0
    if start > end :
        temp = start
        start = end
        end = temp
    if start not in start_list:
        # start_list.append(start)
        heapq.heappush(start_list, start)

    max_value = max(max_value, end)
    
    heapq.heappush(rail_heap, (start, end))


len_L = int(input())

realAnswer = 0
# start_list.sort()
# print(start_list)
# for i in range(len(start_list)):
temp_idx = 0
while start_list :
    print(start_list)
    # print(start_list[i])
    listOfStart = heapq.heappop(start_list)
    if listOfStart + len_L > max_value :
        break
    else:                                           
        if temp_idx != 0:
            rail_heap = callback
        callback = []
        correctCnt = 0
        print(rail_heap)
        while rail_heap :
            temp_idx = 1
            temp_rail = heapq.heappop(rail_heap)
            if temp_rail[0] < listOfStart :
                continue
            elif temp_rail[1] > listOfStart + len_L :
                heapq.heappush(callback, temp_rail) 
            else:
                heapq.heappush(callback, temp_rail)
                correctCnt += 1

        # else:
        #     print("다시 콜백해주는 리스트:", callback)
        #     while callback:
        #         heapq.heappush(rail_heap, heapq.heappop(callback))

        # print("맞은 철로는? : " ,correctCnt)
        realAnswer = max(realAnswer, correctCnt)

print(realAnswer)