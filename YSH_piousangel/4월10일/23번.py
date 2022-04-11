from collections import deque
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

N = int(input())
A = int(input())

board = [[0 for i in range(N)] for _ in range(N)]
visited = [ [False]*N for _ in range(N)]
# print(visited)
# print(board)
if A != 0:
    for i in range(A):
        y, x = map(int, input().split())
        board[y-1][x-1] = 1

R = int(input())
rotation_info = []
move_info = [ [0,1], [1,0], [0,-1], [-1,0] ]  #인덱스0 -> y, 인덱스 1 -> x
for i in range(R):
    num, alpa = map(str, input().split())
    rotation_info.append([num, alpa])

# print("rotation_info", rotation_info)
answer = 0

def bfs(board, visited):
    global answer
    q = deque([])
    visited_q = deque([])
    q.append([0,0,0,0])     #마지막은 시간
    visited[0][0] = True
    visited_q.append([0,0])

    while q :
        y, x, time, info = q.popleft()  #y,x축, 시간, 로테이션 정보
        
        flag = True
        for i in range(len(rotation_info)) :
            rot = rotation_info[i]
            if time == int(rot[0]) :
                flag = False
                if rot[1] == 'D' :
                    #오른쪽 90도 회전
                    info += 1
                    if info == 4:
                        info = 0
                    ny = y + move_info[info][0]
                    nx = x + move_info[info][1]
                    # time += 1
                    break
                elif rot[1] == 'L':
                    #왼쪽 90도 회전
                    info  -= 1
                    if info == -1:
                        info = 3
                    ny = y + move_info[info][0]
                    nx = x + move_info[info][1]
                    # time += 1
                    break          
        if flag:
            ny = y + move_info[info][0]
            nx = x + move_info[info][1]

        answer = time+1
    
        # print(y, x, time, info)
        # print(visited_q)
        if 0 <= ny < N and 0 <= nx < N :
            if visited[ny][nx] != True and board[ny][nx] == 1 :
                visited[ny][nx] = True
                board[ny][nx] = 0
                visited_q.append([ny,nx])
                q.append([ny,nx,time+1, info])
            elif visited[ny][nx] != True and board[ny][nx] == 0 :
                visited[ny][nx] = True
                visited_q.append([ny,nx])
                chkY, chkX = visited_q.popleft()
                visited[chkY][chkX] = False
                q.append([ny,nx,time+1, info])
        
        else:
            return      
          
bfs(board, visited)

print(answer)


