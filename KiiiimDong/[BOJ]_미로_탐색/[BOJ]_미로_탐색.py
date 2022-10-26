from collections import deque

n, m = map(int, input().split()) # n, m을 공백으로 구분하여 입력받기

graph = [] # 그래프(리스트)
for i in range(n):
    graph.append(list(map(int, input()))) # 리스트안에 리스트로 간선 정보 받기

# 이동할 네 방향(상, 하, 좌, 우)정의
dx = [-1, 1, 0, 0] # dx 정의(좌 우)
dy = [0, 0, -1, 1] # dy 정의(상 하)

# BFS 구현
def bfs(x, y):
    queue = deque() # 덱으로 큐 구현
    queue.append((x, y)) # 큐에 x,y 좌표를 튜플로 append(탐색을시작할좌표)

    while queue: # 큐가 빌때까지
        x, y = queue.popleft() # 큐에 append한거 다시 꺼낸거
         
        for i in range(4): # 현재위치에서 4방향으로 확인할거
            nx = x + dx[i] # 현재 x에서 2방향(좌, 우)
            ny = y + dy[i] # 현재 y에서 2방향(상, 하)

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 미로 찾기 공간을 벗어난 경우에 무시
                continue
            if graph[nx][ny] == 0: # 움직일 수 없는 경우 무시
                continue
            if graph[nx][ny] == 1: # 해당노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny] = graph[x][y] + 1 # 현재위치에서 한칸 더 간거
                queue.append((nx, ny)) # nx, ny로 다시 x,y 좌표를 바꿔준다.
    return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단거리

print(bfs(0, 0)) # 원점에서부터 BFS 돌리기.