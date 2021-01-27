n = int(input())

for _ in range(n):
    a = int(input())
    b = int(input())

    arr = [i for i in range(1,b+1)]
    for _ in range(a):
        for x in range(1, b, 1):
            arr[x] = arr[x-1] + arr[x]

    print(arr[b-1])
