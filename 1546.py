n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    sum += x / max(arr) * 100


print(sum/n)