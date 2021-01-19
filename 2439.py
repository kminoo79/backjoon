a = int(input())

for x in range(1, a+1):
    for y in range(a-x):
        print(" ",end="")
    for y in range(x):
        print("*",end="")
    print("")