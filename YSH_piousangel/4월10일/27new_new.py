import sys
import heapq

sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

rail_heap = []
rail_pos = []
for i in range(n):
    s, e = map(int, input().split())
    rail_pos.append((min(s,e), max(s,e)))

main_rail = int(input())
answer = 0
rail_pos.sort(key = lambda x : (x[1], x[0]))

# print(rail_pos)
for i in range(n):

    now_start, now_end = rail_pos[i]

    if now_end - now_start > main_rail:
        continue

    # if rail_pos[i] not in rail_heap:         #중복 확인
    #     heapq.heappush(rail_heap, rail_pos[i])
    if not rail_heap:
        heapq.heappush(rail_heap, rail_pos[i])
        # rail_heap.append(rail_pos[i])
    else:
        while now_end - rail_heap[0][0] > main_rail :
            heapq.heappop(rail_heap)
            if not rail_heap:
                break

        heapq.heappush(rail_heap, (now_start, now_end))
    # print("len : " , len(rail_heap))
    answer = max(len(rail_heap), answer)
    
print(answer)