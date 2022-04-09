import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


m = int(input())

m_list = list(map(int, input().split()))

for m in m_list :
    start = 0
    end = len(n_list)-1
    mid = end // 2
    while end - start >= 0 :

        if m == n_list[mid] :
            print(1)
            break
        elif m > n_list[mid] :
            start = mid+1
        elif m < n_list[mid] :
            end = mid -1

        mid = (end+start)//2

    else:
        print(0)


# for k in m_list :

#     l_idx = 0
#     r_idx = len(n_list)-1
#     m_idx = (r_idx + l_idx) // 2

#     while r_idx >= l_idx :

#         m_idx = (r_idx + l_idx) // 2

#         if k == n_list[m_idx] :
#             print("1")
#             break
#         elif k > n_list[m_idx]:
#             l_idx = m_idx + 1
#         else:
#             r_idx = m_idx - 1
#     else:
#         print("0")

 





























