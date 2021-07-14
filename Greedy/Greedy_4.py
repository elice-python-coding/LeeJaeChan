N, K = map(int, input().split())
n_count = 0

while N != 1:
    if N % K != 1 and (N % K) == 0:
        N = N // K
        n_count += 1
    elif (N % K) >= 1:
        N -= 1
        n_count += 1

print(n_count)
