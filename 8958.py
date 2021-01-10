n = int(input())
arr = [list(input()) for _ in range(n)]
for k in range(n):
    prev = 0
    sum = 0
    for x in range(len(arr[k])):
        if (arr[k][x]== "O" or arr[k][x] == "o"):
            prev += 1
            sum += prev
        else:
            prev = 0
    print(sum)
            
