# [BOJ] RGB거리 (Silver-1)

[문제링크](https://www.acmicpc.net/problem/1149)

## 1. 문제 설명



### 1.1 문제요약

1. 집이 N개 주어진다.
2. 각 집을 R, G, B 중 하나로 칠해야한다.
3. 각 집마다 다른 R, G, B 비용이 주어진다.
4. 각 집은 이웃한 집과 색이 같아서는 안된다.
5. 모든 집을 R, G, B로 칠할 때, 최소 비용을 리턴하시오.

### 1.2 입출력 예시

- 입력

  ```python
  3
  26 40 83
  49 60 57
  13 89 99
  ```
  
- 출력

  ```python
  96
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) Dynamic Programming

- 목표 설정
  - 해당 문제의 목표는 각 집을 규칙에 맞게 R, G, B로 색칠 했을 때, 전체 드는 비용의 최솟값을 구하는 것이다.
- 규칙찾기
  - 해당 문제는 규칙이 난해하다. => 규칙을 찾기 어렵다.
  - 규칙이 찾기 어렵기 때문에 우리가 취해야할 행동은 전수조사이다. 즉, 모든 경우의 수를 확인하여 최솟값으로 설정한다.
  - 해당 문제는 n >= 1일 때, 그 집을 R로 색칠하는 경우, G로 색칠하는 경우, B로 색칠하는 경우로 나누어서 그 값을 구한다.
  - 최종적으로 N번째일 때,
    1. R로 칠했을 경우의 값
    2. G로 칠했을 경우의 값
    3. B로 칠했을 경우의 값
  - 이 남아있게 되는데, 이 중 최솟값을 선택하면 된다.
