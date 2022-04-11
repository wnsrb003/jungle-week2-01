#히스토그램에서 가장 큰 직사각형 
# https://www.acmicpc.net/problem/6549
# 스택
import sys
import copy

# 테스트 = [[2,1,4,5,1,3,3], [1000, 1000, 1000,1000]]
n = []
while True:
    inp = sys.stdin.readline().strip().split()
    if '0' == inp[0]:
        break
    n.append(list(map(int, inp))[1:])

for 그램 in n:
    길이 = []
    최대너비 = 0
    index = 0

    while 그램:
        높이 = 그램.pop()
        if 길이 :
            if 길이[-1][1] <= 높이:
                최대너비 = max(길이[-1][1] * (index - 길이[-1][0] + 1), 최대너비)
                뺀놈 = 길이.pop()
                길이.append((뺀놈[0], 높이))
            else:
                길이.append((index, 높이))
        else :
            길이.append((index, 높이))
        index += 1
    최종길이 = [(index - 길이[-1][0]) * 길이[-1][1]]
    for i in range(1, len(길이)):
        for j in range(i-1, len(길이)):
            최종길이.append((길이[i][0] - 길이[j][0] -1) * 길이[j][1])
    print(길이, max(최대너비, max(최종길이)))

# def 고르기(높이, 그램):
#     global 최대너비
#     if not len(테스트) :
#         return
#     다음 = 테스트.pop()
#     if 다음 * len(그램) <= 최대너비:
#         return
#     # if 높이 * len(그램) <= 최대너비:
#     #     return
#     # if 높이 < 최소높이 :
#     #     최대너비 = max(최대너비, 높이 * len(n))
#     #     return
#     for i in range(len(그램)):
#         if 그램[i] >= 높이:
#             cnt = 1
#             for j in range(i+1, len(그램)):
#                 if 그램[j] < 높이 :
#                     break
#                 else :
#                     cnt += 1
#             최대너비 = max(최대너비, 높이 * cnt)
#     고르기(다음, 그램)
# for i in range(len(n)):
#     # 최대너비 = max(테스트)
#     테스트 = copy.deepcopy(n[i])
#     테스트.sort()
#     최소높이 = min(테스트)
#     최대너비 = max(테스트)
#     고르기(테스트.pop(), n[i])
#     print(최대너비)