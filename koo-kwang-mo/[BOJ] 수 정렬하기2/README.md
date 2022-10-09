# [BOJ] 수 정렬하기 2

> 백준 연습문제

[문제링크](https://www.acmicpc.net/problem/2751)

## 1. 문제 설명
- N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.



### 1.1 문제요약

1. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

### 1.2 입출력 예시

- 입력
  첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
  
- 출력
  첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

<img src='입출력 예시.jpg'>

## 2. 문제해결 아이디어
- 최소 입력되는 N에 대한 readline을 작성하고 sort함수를 활용하여 오름차순으로 정렬한다.


### 1) 문제의 핵심
- sys.stdin.readline을 활용한 시간단축.



+) input과 readline의 차이점.
 - 일단 sys.stdin.readline()과 input()은 같은 역할을 하지 않는다.
 - input() 내장 함수는 parameter로 prompt message를 받을 수 있다
 - 따라서 입력받기 전 prompt message를 출력해야 한다
 - 물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다
 - 하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
 - 또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다
 - 즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다
 - 반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 이 때문에 조금 귀찮은 점이 있기도 하다.


  ==> 결론적으로 input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.


readline 활용 : https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

출처) https://lute3r.tistory.com/m/240
