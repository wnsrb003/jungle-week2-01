from collections import deque

n = int(input())

q = deque()

for i in range(1,n+1):
    q.append(i)

while len(q) >= 2 :

    if len(q) == 2:
        q.popleft()
        break

    q.popleft()
    q.append(q.popleft())

print(q[0])
