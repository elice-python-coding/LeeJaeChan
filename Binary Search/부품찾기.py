import sys
input = sys.stdin.readline

N = int(input())
N_parts = list(map(int, input().split()))

M = int(input())
M_parts = list(map(int, input().split()))

for find_parts in M_parts:
    if find_parts in N_parts:
        print("yes", end=' ')
    else:
        print("no", end=' ')
        