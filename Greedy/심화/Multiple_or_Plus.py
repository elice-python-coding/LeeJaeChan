s = input()
result = int(s[0])              # s의 0번째 인덱스(계속해서 값을 더해갈 기준 인덱스)

for i in range(1, len(s)):
    num = int(s[i])             # 1씩 증가, 인덱스 끝까지 확인
    if result <= 1 or num <= 1: # 0, 1일 때는 *보다 +가 더 높은 값
        result += num
    else:
        result *= num           # 0, 1이 아닐 때는 전부 곱셈 연산

print(result)
