N = int(input())
direction = input().split() # 방향
x = y = 1

for i in direction:
    if i == 'L' and x != 1:
        x -= 1
    elif i == 'R' and x < N:
        x += 1
    elif i == 'U' and y != 1:
        y -= 1
    elif i == 'D' and y < N:
        y += 1
    pass

print(y, x)