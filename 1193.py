x = int(input())
k = 1

while x > k:
    x -= k
    k += 1

if(k%2 == 0):
    print(str(x)+"/"+str(k-x+1))
else:
    print(str(k-x+1)+"/"+str(x))

