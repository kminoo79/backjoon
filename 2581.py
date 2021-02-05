arr = []

m = int(input())
n = int(input())

for x in range(m, n+1, 1):
    if x == 1: pass
    elif x == 2 : arr.append(x)
    else:
        for y in range(2, x, 1):
            if(x % y == 0): break
            elif(y == x-1): arr.append(x)

if(len(arr) == 0): print('-1')
else:
    print(sum(arr))
    print(min(arr))