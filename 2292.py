n = int(input())

c,  room = 1, 1

while n > c:
    c += room *6
    room += 1

print(room)