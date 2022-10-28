# [BOJ] 통계학 (Silver-5)

> .

[문제링크](https://www.acmicpc.net/problem/2108)

## 1. 문제 설명



### 1.1 문제요약

1. N개의 수가 주어진다. 다음을 계산하여 출력하라.
   1. 산술평균
   2. 중앙값
   3. 최빈값
   4. 범위 : 최댓값 - 최솟값의 차이

### 1.2 입출력 예시

- 입력

  ```python
  5
  1
  3
  8
  -2
  2
  ```
  
- 출력

  ```python
  2
  2
  1
  10
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) Python의 수학관련 함수들을 적절하게 이용

- 평균값
  - ``statistics`` 라이브러리의 mean
- 중앙값
  - ``statistics`` 라이브러리의 median
- 최빈값
  - ``collections`` 라이브러리의 Counter
- 차이
  - 기본 라이브러이의 min, max