# [BOJ] 설탕 배달 (Silver-4)

> [ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Asia Regional - Taejon 2001](https://www.acmicpc.net/category/detail/884) PC번

[문제링크](https://www.acmicpc.net/problem/9095)

## 1. 문제 설명



### 1.1 문제요약

1. 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하라.
2. 단, 1 + 2와 2 + 1은 다른 방법으로 취급한다.
3. 0 < n <= 11
4. 입력은 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 정수 n이 주어진다.
5. n은 양수이며 11보다 작다.

### 1.2 입출력 예시

- 입력

  ```python
  3
  4
  7
  10
  ```
  
- 출력

  ```python
  7
  44
  274
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) Dynamic Programming

- 본 문제는 DP를 사용한다.
- DP의 핵심은 문제의 규칙을 찾아서 점화식을 만들고 그것을 코드로 표현하는 것이다.



#### (2) 해당 문제의 규칙

```reStructuredText
n = 1일 때,
1 + 1이므로
1

n = 2일 때,
1 + 1
2 이므로
2

n = 3일 때,
1 + 1 + 1
1 + 2
2 + 1
3 이므로
4

!! 4부터는 1, 2, 3이 단독으로 쓰여질 수 없다.

n = 4일 때,
1 + N(3) => 4
2 + N(2) => 2
3 + N(1) => 1
이므로
7

n = 5일 때,
1 + N(4) => 7
2 + N(3) => 4
3 + N(2) => 2
이므로
13

n = 6일 때,
1 + N(5) => 13
2 + N(4) => 7
3 + N(3) => 4
이므로
24
```

즉, 위의 규칙으로 보면 점화식은 다음과 같다.

N(n) = N(n - 1) + N(n - 2) + N(n - 3)

그러므로 우리는 다음의 점화식을 코드로 나타내면 된다.

