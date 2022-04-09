import heapq
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

f_heap = []
s_heap = []

flag = True
heapq.heappush(f_heap, int(input()))

for i in range(1,n):

    temp = int(input())
    mid_value = 0
    mid_value = (i-1) // 2
    
    # print("mid", mid_value)
    # print(flag)
    if flag == True :
        flag = False
        # for j in range(0,i):
        #     heapq.heappush(f_heap, temp)
        
        for j in range(len(s_heap)):
            k = heapq.heappop(f_heap)
            # if j == mid_value:
            #     print(k)
            print("True",k)
            heapq.heappush(s_heap, k)
    else:
        flag = True
        # for j in range(0,i):
        #     heapq.heappush(s_heap, temp)
        
        for j in range(len(f_heap)-1):
            k = heapq.heappop(s_heap)
            # if j == mid_value:
            #     print(k)
            print("False",k)
            heapq.heappush(f_heap, k)

    
