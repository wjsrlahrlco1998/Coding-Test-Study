# [BOJ] 회의실 배정(Silver-1)

> .

[문제링크](https://www.acmicpc.net/problem/1931)

## 1. 문제 설명



### 1.1 문제요약

1. 한 개의 회의실에 대해 이를 사용하는 회의실 사용표를 만드려고 한다.
2. 입력은 회의의 개수, 각 회의별 시작 시간, 끝나는 시간이 주어진다.
3. 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수를 리턴하라.



### 1.2 입출력 예시

- 입력

  ```python
  11
  1 4
  3 5
  0 6
  5 7
  3 8
  5 9
  6 10
  8 11
  8 12
  2 13
  12 14
  ```
  
- 출력

  ```python
  4
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) 그리디 알고리즘

- > Q. 그리디 알고리즘이란?
  >
  > A. 그리디 알고리즘은 미래의 결과를 생각하지 않고 현재 선택할 수 있는 최선의 결과만을 선택하는 알고리즘이다.

- 본 문제에서는 그리디 알고리즘을 사용하여, 끝나는 시간이 가장 짧은 순, 거기서 시작시간이 가장 빠른 순으로 정렬하여 그 순간 선택할 수 있는 최선의 회의를 선택한다.

- 단, 유의사항으로 회의는 겹치면 안되기 때문에 그 전 회의시간의 끝나는 시간보다 시작하는 시간이 같거나 큰 회의만 다음으로 들어갈 수 있다.