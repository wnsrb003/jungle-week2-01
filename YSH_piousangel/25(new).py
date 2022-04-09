import heapq
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline
maxHeap = []                    #작은수 maxheap으로정렬
minHeap = []                    #큰수 minheap으로 정렬

n = int(input())

# print(heapq.heappop(heap)[1])    

for i in range(n):
    V = int(input())

    if len(maxHeap) == len(minHeap) :
        if len(minHeap) == 0 :
            heapq.heappush(maxHeap, (-V,V))
        else:
            if minHeap[0] > V :
                heapq.heappush(maxHeap, (-V,V))
            else:
                temp = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-temp, temp))
                heapq.heappush(minHeap, V)
    else:
        if V > maxHeap[0][1] :
            heapq.heappush(minHeap, V)
        else:
            heapq.heappush(minHeap, heapq.heappop(maxHeap)[1])
            heapq.heappush(maxHeap, (-V,V))

    print(maxHeap[0][1])
            