import heapq

n = int(input())

card_heap = []
for i in range(n):
    heapq.heappush(card_heap, int(input()))
sum = 0
while len(card_heap) > 1:
    temp = heapq.heappop(card_heap)+ heapq.heappop(card_heap)
    sum += temp
    heapq.heappush(card_heap, temp)

print(sum)