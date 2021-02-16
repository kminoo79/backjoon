n = int(input())

arr = [list(input().split()) for _ in range(n)]

for x in range(n):
    for y in range(len(arr[x][1])):
        for z in range(len(arr[x][0])):
            print(arr[x][1][y:y+1] * int(arr[x][0]),end="")
    print("")


# 다른 이상적인 답 (시간 복잡도가 낮음)

# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i