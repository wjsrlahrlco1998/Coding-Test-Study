# [BOJ] 문자열 집합 (Silver-3)

> .

[문제링크](https://www.acmicpc.net/problem/14425)

## 1. 문제 설명



### 1.1 문제요약

1. 문자열의 개수 N, M이 주어진다.
2. 먼저 주어지는 N개의 문자열은 집합 S에 포함된 문자열로 중복이 없다.
3. 다음에는 M개의 문자열이 주어진다.
4. M개의 문자열 중 집합 S에 포함되는 문자열은 몇개인지 출력하는 프로그램을 작성하라.

### 1.2 입출력 예시

- 입력

  ```python
  5 11
  baekjoononlinejudge
  startlink
  codeplus
  sundaycoding
  codingsh
  baekjoon
  codeplus
  codeminus
  startlink
  starlink
  sundaycoding
  codingsh
  codinghs
  sondaycoding
  startrink
  icerink
  ```
  
- 출력

  ```python
  4
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) 문제의 파악이 중요하다.

- 집합 S에 포함되는 N개의 문자열은 중복이 없고, 다음에 오는 M개의 문자열은 중복이 있을 수 있음에 유의하여야한다.