import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline
A, B, C = map(int, input().split())
answer = 1
                           #어떻게 성능 개선을 해야할지 잘 모르겠습니다.
def dfs(A, B):
    global answer

    if B == 1:
        return A
        
    if B%2 != 0 :   
        return dfs(A,B//2) * dfs(A,B//2) * A
    else:
        return dfs(A,B//2) * dfs(A,B//2)
    
answer = dfs(A, B)
# print(answer)
print(answer % C)



