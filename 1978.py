n = int(input())                        
arr = list(map( int, input().split())) 
count = 0

for a in arr:                          
    if (a == 1): count +=1

    for i in range(2, a, 1):
        if(a%i == 0): 
            count += 1
            break

print(n - count)
    
    