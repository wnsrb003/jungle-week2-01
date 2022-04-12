import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, C = map(int, input().split())

n_list = [int(input()) for i in range(N)]

n_list.sort()

start = 1
end = n_list[len(n_list)-1] - n_list[0]

answer = 0

while start <= end :

    mid = (end + start) // 2
    left_wifi = C - 1
    nowhome = n_list[0]
    for i in range(1, N) :
        if n_list[i] - nowhome >= mid :
            nowhome = n_list[i]
            left_wifi -= 1
        if left_wifi == 0:
            break

    if left_wifi == 0:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)