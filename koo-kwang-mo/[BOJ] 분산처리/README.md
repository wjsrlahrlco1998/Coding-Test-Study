# [BOJ] 분산 처리

> 백준 연습문제

[문제링크](https://www.acmicpc.net/problem/1009)

## 1. 문제 설명
- 재용이는 최신 컴퓨터 10대를 가지고 있다. 어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.

1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,

10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

총 데이터의 개수는 항상 ab개의 형태로 주어진다. 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 이를 수행해주는 프로그램을 작성하라.



### 1.1 문제요약

1. 주어진 두 숫자에 a,b에 대해서 a**b의 일의 자리 숫자를 출력하라.


### 1.2 입출력 예시

- 입력
  입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다. (1 ≤ a < 100, 1 ≤ b < 1,000,000)
  
- 출력
  각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.

<img src='입출력 예시.JPG'>

## 2. 문제해결 아이디어
- 처음 생각한 방법은 a**b에 대해서 10으로 나눈 나머지를 출력하는 것이었다.
- 하지만 b가 커짐에 따라 시간 및 메모리에 대해서 한계가 생겼다.
- 때문에 a에 대한 케이스를 분류함으로써 시간을 단축하였다.
<img src='a케이스 예시.JPG'>
- 케이스 분류를 통해 적게는 한 번 많게는 네 번 반복하는 경우의 수를 적용하여 네 제곱까지 연산으로
- 결과를 얻을 수 있다.

### 1) 문제의 핵심
- 분산처리
