# 아 ... 떡볶이 먹고 싶다 (배고파;) // 그나저나 96년생 동빈이 겁나 바쁨
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
length = list(map(int,input().split())) # 19 15 10 17

Start_point = 0
Cutter_point = 0 # 결과적으로 절단기의 높이 값이 담길 변수
End_point = max(length) # 가장 큰 값을 기준으로 전체 범위가 설정
Rise_cake = 0

while(Start_point <= End_point):
    Center = (Start_point + End_point) // 2
    for R_c_height in length:
        if R_c_height > Center: # [19, 15, 10, 17] > 9
            Rise_cake += R_c_height - Center
        else:
            pass
    
    if Rise_cake < M:
        End_point = Center - 1 # 엔드포인트 이동 (떡이 적을 때)
    else:
        Cutter_point = Center
        start_point = Center + 1 # 스타트 포인트 이동 (떡이 많을 때)

print(Cutter_point)