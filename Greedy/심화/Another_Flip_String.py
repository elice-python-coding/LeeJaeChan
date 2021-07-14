s = input()
ZeroCount = OneCount = 0
WildCard = 0

if s[0] == '1':
    WildCard = 1

for i in range(len(s) - 1):
    # index[0]이 0일 때, index[-1]가 0이라면(홀수) 1의 횟수(짝수)가 적다
    # index[0]이 0일 때 index[-1]가 1이라면 동일
    if int(s[0]) == WildCard and int(s[-1]) == 0:
        if int(s[i]) == 1 and int(s[i + 1]) == 0:
            OneCount += 1
        elif int(s[i]) == 0 and int(s[i + 1]) == 1:
            ZeroCount += 1

    elif int(s[0]) == WildCard and int(s[-1]) == 1:
        if int(s[i]) == 1 and int(s[i + 1]) == 0:
            OneCount += 1
        elif int(s[i]) == 0 and int(s[i + 1]) == 1:
            ZeroCount += 1
    
print(max(ZeroCount, OneCount))