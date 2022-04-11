N, T = map(int, input().split())

char_list = []
for i in range(N):
    char_list.append(int(input()))

char_list.sort()

mid_level = sum(char_list) // len(char_list)

answer = 0
cnt = 1

left_idx = 0
right_idx = len(char_list)-1

max_value = char_list[-1]

while left_idx < right_idx :

    mid_idx = (right_idx+left_idx) // 2
    total = 0
    for i in range(mid_idx+1):
        total += char_list[i]
    
    total = char_list // (mid_idx+1)