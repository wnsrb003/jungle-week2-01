import heapq
import sys
sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())
ans = 0
positions = [] 
for _ in range(n):
    p1, p2 = map(int, input().split())
    positions.append((min(p1, p2), max(p1, p2)))

positions.sort(key = lambda x: (x[1], x[0]))        #두번째 값으로 정렬 후 첫번째 값으로 정렬
d = int(input())

ans = 0
print(positions)
acc = []
for i in range(n): 
    next_s, next_e = positions[i]
    print("next_s", next_s, "next_e", next_e)
    # print()
    if next_e - next_s > d :
        continue

    if not acc :                             #A, B집 위치가 같을 수도 있습니다.
        # acc.append(positions[i])
        heapq.heappush(acc, positions[i])

    else:
        while next_e - acc[0][0] > d: 
            heapq.heappop(acc)
            if not acc :
                break
    
        heapq.heappush(acc, (next_s, next_e))

    ans = max(ans, len(acc))

print(ans)

