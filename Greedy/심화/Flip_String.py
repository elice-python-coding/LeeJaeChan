s = input()
ZeroCount = 0
OneCount = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            OneCount += 1
        else:
            ZeroCount += 1

print(min(ZeroCount, OneCount))
