n = int(input())

count = 0

for i in range(1, n+1):
    arr = list(str(i))
    if(len(arr) <3): count += 1
    elif(int(arr[0]) - int(arr[1]) == int(arr[1]) - int(arr[2])):
        count +=1
    else:
        pass

print(count)