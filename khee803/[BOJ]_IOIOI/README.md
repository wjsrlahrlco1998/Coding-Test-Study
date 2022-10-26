# [BOJ] IOIOI - 5525 (Silver IV

[문제링크](https://www.acmicpc.net/problem/5525)

## 1. 문제 설명
### 1.1 문제요약
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

- P1 IOI
- P2 IOIOI
- P3 IOIOIOI
- PN IOIOI...OI (O가 N개)
  
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.


### 1.2 입출력 예시

- 입력

  ```python
  1
  13
  OOIOIOIOIIOII
  ```

- 출력

  ```python
  4
  ```

- 입력

  ```python
  2
  13
  OOIOIOIOIIOII
  ```

- 출력

  ```python
  2
  ```


## 2. 문제해결 아이디어
- 'IOI'라는 문자열을 기준으로 두어 S[i-1], S[i], S[i+1]을 확인하며 'IOI'와 일치하는지 확인하고 카운트를 체크하는 방식으로 해결
