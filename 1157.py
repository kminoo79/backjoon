N = input().upper()
arr = {}
string = []

for x in N:
    if(x in string): arr[x] += 1
    else: 
        string.append(x)
        arr[x] = 1
arr2 = dict(map(reversed, arr.items()))

print(arr)
print(arr2[max(arr2.keys())])
print(arr2)