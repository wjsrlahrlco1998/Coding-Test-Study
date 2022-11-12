import sys
from collections import deque#BFS활용을 위한 덱 임포트

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]#땅들의 높이 받아옴

cur_max = 0#땅의 최대 높이
for i in range(N):
    for j in range(N):
        cur_max = max(cur_max, graph[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def bfs(x, y, k):
    cnt = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > k and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    cnt += 1
                    visited[nx][ny] = 1

    return cnt


res = 0
for k in range(cur_max + 1):#물의 최대 높이 지정
    visited = [[0] * N for _ in range(N)]#방문 리스트 만들기
    res_cnt = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:#방문한 적 없는 안전영역이라면
                res_cnt.append(bfs(i, j, k))
                cnt = 0
    res = max(res, len(res_cnt))

print(res)