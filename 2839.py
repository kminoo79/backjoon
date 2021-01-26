n = int(input())
arr = []

for a in range(0, int(n//3)+1):
    b = (n - 3 *a) / 5
    if(b == int(b)): arr.append(a+b)

if(len(arr) != 0): print(int(min(arr)))
else: print(-1)
