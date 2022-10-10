# [BOJ] 바이러스 (Silver-3)

> [Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2004](https://www.acmicpc.net/category/74) > [초등부](https://www.acmicpc.net/category/detail/379) 3번

[문제링크](https://www.acmicpc.net/problem/2606)

## 1. 문제 설명



### 1.1 문제요약

1. N개의 컴퓨터와 N개의 컴퓨터가 이어져있는 정보가 주어진다.
2. 웜 바이러스는 X번째의 컴퓨터에 걸리면, X번째와 이어져있는 모든 컴퓨터에 전염된다.
3. 1번 컴퓨터가 웜 바이러스에 감염되었을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라.

### 1.2 입출력 예시

- 입력

  ```python
  7
  6
  1 2
  2 3
  1 5
  5 2
  5 6
  4 7
  ```
  
- 출력

  ```python
  4
  ```
  
  

## 2. 문제해결 아이디어



### 1) 문제의 핵심



#### (1) 그래프 탐색 알고리즘 적용

- 해당 문제는 1번 노드와 이어진 모든 노드를 한번씩 탐색하면 되는 문제이다.
- 따라서, DFS또는 BFS 알고리즘을 통해서 연결된 노드를 한번씩 방문한다.
- 필자는 BFS 알고리즘을 deque로 구현하여 사용하였다.