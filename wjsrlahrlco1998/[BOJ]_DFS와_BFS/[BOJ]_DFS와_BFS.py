import sys
from collections import deque
import time

read = sys.stdin.readline

# 1. 정점의 개수(N), 간선의 개수(M), 탐색을 시작할 정점 번호(V) 입력 : 1 <= N <= 1000, 1 <= M <= 10000
N, M, V = map(int, input().split())

# 2. 인접 0행렬 생성
matrix = [[0] * (N + 1) for _ in range(N + 1)]

# 3. 방문한 곳을 확인하기 위한 배열 선언
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)

# 4. 인접 행렬 입력
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

# 5. DFS 정의
def dfs(V):
    # 1) 방문 표시
    visited_1[V] = 1

    print(V, end=' ')

    # 2) 재귀함수를 이용한 탐색
    for i in range(1, N + 1):
        if(visited_1[i] == 0 and matrix[V][i] == 1):
            dfs(i)

# 6. BFS 정의
def bfs(V):
    # 1) 방문해야 할 곳을 순서대로 넣을 큐
    queue = deque()
    queue.append(V)

    # 2) 방문 표시
    visited_2[V] = 1

    # 3) 큐 안에 데이터가 없을 때까지 반복
    while queue:
        V = queue.popleft()
        print(V, end = " ")
        
        for i in range(1, N + 1):
            if visited_2[i] == 0 and matrix[V][i] == 1:
                queue.append(i)
                visited_2[i] = 1

# 7. 실행
dfs(V)
print()
bfs(V)