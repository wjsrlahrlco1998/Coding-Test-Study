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
    while q:# 연결되어 있는 칸에 대한 탐색이 종료될 때까지
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


res = 0#출력값, 최대값을 비교해야 하기 때문에 초기 값 0 설정.
for k in range(cur_max + 1):#물의 최대 높이 지정
    visited = [[0] * N for _ in range(N)]#방문 리스트 만들기
    res_cnt = []#안전영역의 높이 저장
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:#방문한 적 없는 안전영역이라면 진행, 방문기록을 진행하지 않으면 한 개의 안전영역에 대해서 여러번 탐색하게 됨.
                res_cnt.append(bfs(i, j, k))#한 영역의 땅의 갯수 저장.
                cnt = 0
    res = max(res, len(res_cnt))#1~cur_max 까지의 물 높이에 따른 안전영역 갯수 비교 및 최대값 저장.

print(res)