import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shooting_points = list(map(int, input().split()))
shooting_points.sort()
animal_points = [tuple(map(int, input().split())) for _ in range(n)]


def check(x, y):
    start = 0
    end = m - 1
    is_possible = False
    while start <= end:
        mid = (start + end) // 2
        dis = abs(shooting_points[mid] - x) + y
        if dis <= l :
            is_possible = True
            break
        if shooting_points[mid] > x :
            end -= 1
        elif shooting_points[mid] < x :
            start += 1
    return is_possible


ans = 0
for animal_point in animal_points:
    x, y = animal_point
    if y > l :
        continue
    if (x < shooting_points[0] - 4) or (x > shooting_points[-1] + 4):
        continue

    if check(x, y):
        ans += 1

print(ans)


# def find_idx(target):
#     start = 0
#     end = m - 1
#     ans = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if shooting_points[mid] == target:
#             ans = mid
#             break
#         if shooting_points[mid] > target:
#             ans = mid
#             end = mid -1
#         else:
#             start = mid + 1
    
#     return ans

# def find_from_right(start, end, x, y):
#     is_possible = False
#     while start <= end:
#         mid = (start + end) // 2
#         distance = abs(shooting_points[mid] - x) + y
#         if distance <= l:
#             is_possible = True
#             break
#         start 



# ans = 0
# for animal_point in animal_points:
#     ## 범위 안에 있는 거 지우고 시작
#     x, y = animal_point
#     if y > l :
#         continue
#     if x < shooting_points[0] - 4 or x > shooting_points[-1]:
#         continue

#     upper_point = find_idx(x)
#     if upper_point == x:
#         ans += 1
#         continue


    ## 자기 기준으로 왼쪽에서 


    ## 자기 기준으로 오른쪽에서
    # print()
    ## 이 점에 대해서 사대의 인덱스를 알아야해 










