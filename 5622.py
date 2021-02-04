arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
count = 0

for x in a:
    for i in range(8):
        if(x in arr[i]): count += 3 + i

print(count)
