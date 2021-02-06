def ch(k):
    sum = int(k)
    if(len(k) == 1): return int(k) + int(k)
    else:
        for x in k:
            sum += int(x)
        return sum

n = int(input())

arr = []

for x in range(1, n+1, 1):
    if(ch(str(x)) == n): arr.append(x)

if(len(arr) == 0): print(0)
else: print(min(arr))
