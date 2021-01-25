n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(n):
    if(arr[_][2] % arr[_][0] != 0): 
        y = arr[_][2] % arr[_][0]
        x = arr[_][2] // arr[_][0] + 1
    else: 
        y = arr[_][0]
        x = arr[_][2] // arr[_][0]
    

    if (x < 10): print(int(str(y)+ '0' + str(x)))
    else: print(int(str(y)+ str(x)))

