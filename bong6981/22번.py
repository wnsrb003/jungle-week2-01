import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])

answer = []
while len(q) != 0:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(str(q.popleft()))

print("<"+", ".join(answer)+">")
