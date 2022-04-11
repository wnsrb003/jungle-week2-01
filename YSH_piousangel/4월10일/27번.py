import sys
import heapq
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
        start_list.append(start)
    min_value = min(min_value, start)
    max_value = max(max_value, end)
    
    heapq.heappush(rail_heap, (start, end))


len_L = int(input())
# print(min_value, max_value)
realAnswer = 0
start_list.sort()
print(start_list)
for i in range(len(start_list)):
    print(start_list[i])
    if start_list[i] + len_L > max_value :
        break
    else:                                           #최소힙으류 구현했는데 콜백을 너무 많이 하는 것 같기도...

        callback = []
        correctCnt = 0
        while rail_heap :
              
            temp_rail = heapq.heappop(rail_heap)
            # print(temp_rail[0], temp_rail[1])

            if temp_rail[0] < start_list[i] :
                # heapq.heappop(rail_heap)[0]
                continue
            elif temp_rail[1] > start_list[i] + len_L :
                callback.append(temp_rail)      
            else:
                callback.append(temp_rail)
                # print(callback)
                correctCnt += 1

        else:
            print("다시 콜백해주는 리스트:", callback)
            for j in range(len(callback)):
                
                heapq.heappush(rail_heap, callback[j])
        print("맞은 철로는? : " ,correctCnt)
        realAnswer = max(realAnswer, correctCnt)

print(realAnswer)