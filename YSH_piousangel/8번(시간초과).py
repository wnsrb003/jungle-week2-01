import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline
A, B, C = map(int, input().split())
answer = 1
                           #어떻게 성능 개선을 해야할지 잘 모르겠습니다.
def dfs(A, B):
    global answer

    if B == 1:
        return A % C
       
    recur = dfs(A,B//2)
        
    if B%2 != 0 :   
        return recur * recur * A % C
    else:
        return recur * recur % C
    
answer = dfs(A, B)
# print(answer)
print(answer % C)



