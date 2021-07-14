N = input()
x = ord(N[0])-96 # X축
y = N[1] # Y축

move_point = 0 # 이동이 가능하면 1증가
direction = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), ( -1, 2), (1, 2)] # 이동할 위치

for move in direction:
    x = move[0] # direction[[x, ]]
    y = move[1] # direction[[, y]]
    if x > 0 and x < 9 and y > 0 and y < 9: # 이동가능 조건
        move_point += 1

print(move_point)
