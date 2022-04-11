#탑
#https://www.acmicpc.net/problem/2493
#스택
import sys
n = int(sys.stdin.readline().strip())
탑 = list(map(int, sys.stdin.readline().strip().split()))
결과 = [0]*n
while len(탑) >1:
    뺀놈 = 탑.pop()
    for i in range(len(탑)-1, 0, -1):
        if 탑[i] >= 뺀놈:
            결과[len(탑)] = i+1
            break

print(' '.join(list(map(str, 결과))))
