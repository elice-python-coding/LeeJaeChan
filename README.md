# 이취코테 알고리즘 스터디

## 복잡도
직접적으로 알고리즘 문제를 풀어보기에 앞서 알아야할 것이 있다<br>
알고리즘의 성능을 나타낼 수 있는 복잡도(Complexity)이다<br>
일반적으로 복잡도가 낮을수록 좋은 알고리즘인데, 복잡도는 다시 시간 복잡도와 공간 복잡도로 나누어 생각해 볼 수 있다<br>
<br>
* __시간 복잡도__ : 입력 값의 크기에 따라 얼마나 오래 걸리는지를 표현
* __공간 복잡도__ : 입력 값에 대하여 알고리즘이 차지하는 메모리를 표현<br>
<br>
## 시간 복잡도
일반적으로 알고리즘 문제에서 복잡도라고 하면 시간 복잡도를 의미한다<br>
시간 복잡도를 표현할 때는 __빅오(Big-O)표기법__ 을 사용한다<br>
<br>
시간 복잡도가 O(N)이라고 할 때, N = 5라고 가정<br>
이때 변수에 값을 대입, 출력하는 연산 과정이 있지만 상대적으로 N이 커짐에 따라 무시할 수 있을정도로 작아지기 때문에, 가장 영향력이 큰 부분인 N에 비례하는 연산 과정만 시간 복잡도를 표기한다

```python
a = b = 5
print(a + b)
```
위 소스코드의 연산 횟수는 1번으로 시간 복잡도는 O(1)로 표현할 수 있다<br>

```python
arr = [1, 2, 3, 4, 5]

for i in arr:
    for j in arr:
        ex = i * j
        print(ex)
```
위 소스코드는 arr(리스트 변수의 길이) N(5)개일 때, O(N^2)의 시간 복잡도를 가진다<br>
5개의 원소를 2중 반복문을 이용해 매번 곱셈을 하기 때문에 5 × 5가 되는 것이다<br>
(만약 반복문 내에서 다른 함수를 호출하게 된다면 해당 함수의 시간 복잡도까지 고려해야 한다)<br>

시간 복잡도에 따라 명칭이 다르다<br>

| 빅오 표기법  | 명칭           |
| :----------- | -------------- |
| O(1)         | 상수 시간      |
| O(logN)  | 로그 시간      |
| O(N)         | 선형 시간      |
| O(NlogN) | 로그 선형 시간 |
| O(N^2)   | 이차 시간      |
| O(N^3)   | 삼차 시간      |
| O(2^n)   | 지수 시간      |

(차수가 작은 차항을 완전히 무시하는 것도 빅오 표기법이 <u>__항상 절대적이진 않기 때문__</u>에 주의)<br>
<br>
<br>

(8.7.21 1차 저장)



## 그리디(Greedy)
- 현재 상황에서 "지금 당장" 가장 좋아보이는 것만을 선택하는 알고리즘<br>
  즉, 현재의 선택에 의해 나중에 미칠 영향에 대해서는 고려하지 않는다<br>
  <br>
### Q 거스름돈
당신은 점원, 현재 거스름돈으로 사용할 500, 100, 50, 10(원) 동전히 "무한히" 존재한다 <br>
손님에게 N원을 거슬러줘야 할 때 필요한 동전의 최소 개수를 구하라<br>
단, 거슬러 줘야 할 돈 N은 항상 10의 배수<br>

```python
N = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N // coin
    N %= coin

print(count)
```
(굉장히 간단하면서도 직관적인 코드로 작성할 수 있었다)<br>
화폐의 종류(coin_types)만큼 반복을 수행을 하기 때문에 화폐의 종류가 X개라고 할 때<br>
위 코드의 시간 복잡도는 O(X)라고 할 수 있다

(8.7.21 1차 저장)
