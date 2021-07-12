arr_n, M, K = map(int,input().split())
arr = list(map(int, input().split()))

arr.sort()
arr_sum = 0
arr_count = 0

for j in range(M):
    if K != arr_count:
        arr_sum = arr_sum + arr[-1]
        arr_count += 1
    else:
        arr_sum = arr_sum + arr[-2]
        arr_count = 0

print(arr_sum)
