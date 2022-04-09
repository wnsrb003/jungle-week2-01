import sys
sys.setrecursionlimit(10*7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

trees, lens = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()
min_v = 0
max_v = tree_list[-1]

def dfs(tree_list, min_v, max_v, temp_value) :
    global answer

    if min_v > max_v :
        answer = max_v
        return 

    mid_v = (max_v + min_v) // 2

    print(min_v, max_v, mid_v)

    for i in range(len(tree_list)) :
        if tree_list[i] > mid_v :
            temp_value += tree_list[i] - mid_v
    
    if temp_value >= lens :
        dfs(tree_list, mid_v+1, max_v, 0)
    else :
        dfs(tree_list, min_v, mid_v-1, 0)

     
dfs(tree_list, min_v, max_v, 0)
print(answer)