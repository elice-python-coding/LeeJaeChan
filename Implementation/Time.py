N = int(input())
Time_count = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                Time_count += 1

print(Time_count)
