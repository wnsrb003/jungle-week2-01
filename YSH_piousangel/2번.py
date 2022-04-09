import sys
sys.setrecursionlimit(10*7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

trees, lens = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()
min_v = 0
max_v = tree_list[-1]
answer = 0

while min_v <= max_v :

    mid_v = (max_v+min_v) // 2
    total = 0

    for trees in tree_list :
        if trees > mid_v :
            total += trees - mid_v
    
    if total == lens:
        answer = mid_v
        break

    elif total  >= lens :
        min_v = mid_v + 1
        answer = mid_v
    else:
        max_v = mid_v - 1

print(answer)