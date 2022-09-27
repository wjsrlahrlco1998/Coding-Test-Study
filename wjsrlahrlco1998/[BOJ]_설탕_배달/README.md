# [BOJ] 설탕 배달 (Silver-4)

> [Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2010/2011](https://www.acmicpc.net/category/20) > [Contest #7](https://www.acmicpc.net/category/detail/81) 1번

[문제링크](https://www.acmicpc.net/problem/2839)

## 1. 문제 설명



### 1.1 문제요약

1. 설탕의 무게 N(3<=N<=5000)kg이 주어진다.
2. 3kg 봉지와, 5kg의 봉지가 있다.
3. 주어진 설탕을 최소개의 봉지를 사용하여 나누어서 그 최솟값을 반환하라.
4. 만약, 3kg과 5kg의 봉지로 나누어 떨어지게 담을 수 없는 경우 -1을 리턴하라.

### 1.2 입출력 예시

- 입력

  ```python
  18
  4
  6
  9
  11
  ```
  
- 출력

  ```python
  4
  -1
  2
  3
  3
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) Dynamic Programming

- 본 문제는 DP 또는 greedy 알고리즘으로 해결할 수 있다.
- 필자는 DP를 사용하였다.
- DP의 동작 원리를 이해하는 것이 중요하다.
