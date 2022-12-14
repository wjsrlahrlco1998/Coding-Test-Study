# [BOJ] 유기농 배추 심기

> 백준 연습문제

[문제링크](https://www.acmicpc.net/problem/1012)

## 1. 문제 설명
- 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

<img src='문제 예시.JPG'>

### 1.1 문제요약

1. 배추밭에서 상하좌우 1칸씩을 포함하는 범위에 영향을 주는 벌레를 뿌릴 시 가장 효율적으로 벌레를 배치할 수 있도록 하자.

### 1.2 입출력 예시

- 입력
  입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
  
- 출력
  각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

<img src='입출력 예시.JPG'>

## 2. 문제해결 아이디어
- map(int, input().split())을 활용하여 배추밭을 형성하는 M,N,K 에 대한 값을 입력받는다.
- 상하좌우로 움직이는 총 4가지 경우에 대한 함수 dfs를 정의한다.
- 배추밭 전체에 대한 전수조사를 통해 DFS를 적용시킨 후 배추에 적용 될 때 마다 사용된 벌레의 마리 수 cnt를 카운트한다.
- 파이썬의 기본적인 재귀 한도는 1000이며 sys.setrecursionlimit(10000)를 통해 한도를 늘릴 수 있다.
- 

### 1) 문제의 핵심
- DFS의 활용

+) DFS, BFS에 대한 설명
https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html

문제풀이에 대한 설명 출처: https://hei-jayden.tistory.com/100
