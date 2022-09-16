# [PGS] JadenCase 문자열 만들기 (Level - 2)

> Programmers 연습문제

[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12951)

## 1. 문제 설명



### 1.1 문제요약

1. 길이가 1이상 200이하인 문자열이 주어진다.
2. 문자열은 공백, 숫자, 문자로 이루어져있다.
3. 해당 문자열의 첫글자만 대문자로 변환하고 나머지는 모두 소문자여야한다.

### 1.2 입출력 예시

- 입력

  ```python
  "3people unFollowed me"
  ```
  
- 출력

  ```python
  "3people Unfollowed Me"
  ```

  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) python의 lower와 upper 함수

- 파이썬의 lower함수는 모든 문자를 소문자로 변환하는 함수이다.
- upper함수는 모든 문자를 대문자로 변환하는 함수이다.



#### (2) 리스트 자르기

- 문자열의 경우 배열의 각 원소에 할당을 하는 것이 불가능하다. 따라서 첫 문자를 대문자로 변환시킨 문자와 나머지 문자를 이어 붙여서 새로운 변수를 선언해야한다.