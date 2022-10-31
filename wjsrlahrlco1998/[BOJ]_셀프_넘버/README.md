# [BOJ] 셀프 넘버 (Silver-5)

> [ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [North America](https://www.acmicpc.net/category/8) > [Mid-Central Regional](https://www.acmicpc.net/category/37) > [1998 Mid-Central Regional Programming Contest](https://www.acmicpc.net/category/detail/154) D번

[문제링크](https://www.acmicpc.net/problem/4673)

## 1. 문제 설명



### 1.1 문제요약

1.  생성자는 d(n) = n + "n의 각 자리수"로 만들어진다.

2.  1부터 10000까지의 숫자 중 생성자가 아닌 수를 Self Num이라고 한다.
3. 10000이하의 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하라.

- 입력

  ```python
  
  ```
  
- 출력

  ```python
  1
  3
  5
  7
  9
  20
  31
  42
  53
  64
   |
   |       <-- a lot more numbers
   |
  9903
  9914
  9925
  9927
  9938
  9949
  9960
  9971
  9982
  9993
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) 문제의 이해

- Self Num이 무엇인지에 대한 이해가 필요하다.



#### (2) 집합

- Set 자료형의 경우, '-' 차집합, '+' 합집합 등의 연산을 할 수 있다. 이를 이용하자. 또한 중복이 없는 성질또한 이용할 수 있다. 