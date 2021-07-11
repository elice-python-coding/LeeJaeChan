height, width = map(int, input().split()) # 행과 열

first = second = 0

for i in range(height):
    for j in range(1):
        arr = list(map(int, input().split()))
        if len(arr) != width: # 변수 width를 사용해보기 위한 조건 ..
            break
        if first == 0 and second == 0:
            first = min(arr)
        else:
            second = min(arr)
            if first < second:
                first, second = second, first

print(first)
