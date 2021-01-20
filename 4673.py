def ch(k):
    for x in list(str(k)):
        k += int(x)
    return k
    
arr= [ch(_) for _ in range(1, 10001)]

for x in range(1, 10001):
    if x in arr: pass
    else: print(x)