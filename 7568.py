n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
s = []

for x in range(n):
    c = 1
    for y in range(n):
        if((arr[x][0] < arr[y][0]) and (arr[x][1] < arr[y][1])): c+=1
        elif(x == y): pass
    s.append(c)

for _ in range(n):
    print(s[_], end=" ")