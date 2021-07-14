s = input()
ZeroCount = 0
OneCount = 0

for i in range(len(s)-1):
    # 현재 인덱스와 다음 인덱스가 같지 않다면 실행, 같다면 pass
    if s[i] != s[i+1]:
        # 이 때, 0이라면 1이 적고, 1이라면 0이 적다
        if s[i+1] == '0':
            OneCount += 1
        else:
            ZeroCount += 1

print(min(ZeroCount, OneCount))
