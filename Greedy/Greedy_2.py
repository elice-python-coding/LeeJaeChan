arr_n, M, k = map(int,input().split())
arr = list(map(int, input().split()))

for i in range(arr_n-1):
    if i < len(arr):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i], arr[i+1] = arr[i+1], temp
        else:
            pass
    else:
        pass

arr_sum = 0
arr_count = 0

for j in range(M):
    if k != arr_count:
        arr_sum = arr_sum + arr[-1]
        arr_count += 1
    else:
        arr_sum = arr_sum + arr[-2]
        arr_count = 0

print(arr_sum)
