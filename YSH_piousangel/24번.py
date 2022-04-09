import heapq
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    
    n = int(input())

    if n == 0 :
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n,n))

        

