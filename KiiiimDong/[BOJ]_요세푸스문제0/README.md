# 요세푸스문제0
[문제링크](https://www.acmicpc.net/problem/11866)

## 1. 문제 설명

### 1.1 문제요약
- 요세푸스 문제는 다음과 같다.

- 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

- N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.




### 1.2 입출력 방식 
- 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)
- 예제와 같이 요세푸스 순열을 출력한다.

### 1.3 입출력 예시
<img src='입출력예시.jpg'>

## 2. 문제해결 아이디어

### 2.1 우선 큐를 하나 만들어주어 거기에 1부터 N까지 수를 넣어준다.

- 그리고 입력받은 K번째가 되기 전까지 요소를 빼서 뒤로 넘겨주고, K번째가 되면 그 숫자를 result 배열에 넣어준다.

- 그렇게 큐가 빌 때까지 반복한다.

- result 배열을 형식에 맞춰서 출력한다.