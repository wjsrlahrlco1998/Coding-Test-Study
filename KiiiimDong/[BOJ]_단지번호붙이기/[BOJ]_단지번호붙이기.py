from collections import deque

# BFS 구현
def bfs(graph, x, y, index):
    queue = deque() # 덱으로 큐 구현
    queue.append((x, y)) # 큐에 x,y 좌표를 튜플로 append(탐색을시작할좌표)
    cnt = 0 # 단지에 있는 집개수 세주는 변수 
    flag = False # cnt를 반환할 때 조건으로 걸어주려고.

    while queue: # 큐가 빌때까지
        x, y = queue.popleft() # 큐에 append한거 다시 꺼낸거
        
        for i in range(4): # 현재위치에서 4방향으로 확인할거
            nx = x + dx[i] # 현재 x에서 2방향(좌, 우)
            ny = y + dy[i] # 현재 y에서 2방향(상, 하)

            if nx < 0 or ny < 0 or nx >= n or ny >= n: # 그래프 공간을 벗어난 경우에 무시
                continue
            if graph[nx][ny] == 0: # 움직일 수 없는 경우 무시
                continue
            if graph[nx][ny] == 1: # 해당노드를 처음 방문하는 경우에만 집의 개수를 센다.                
                flag = True # cnt 반환하기 위해서
                cnt += 1 # 단지내의 집의 개수 세준다.
                graph[nx][ny] = index # 1이였던 애들을 다른 숫자(2,3,4)로 바꿔준다.
                queue.append((nx, ny))# nx, ny로 다시 x,y 좌표를 바꿔준다.
    if flag: # 반복문을 다 돌고 나와서 flag = True이면 cnt 반환
        return cnt
    else: # flag = False 일때는 cnt 반환하지 않는다.
        return 1
n = int(input())

graph = [] # 그래프(리스트)
for i in range(n):
    graph.append(list(map(int, input()))) # 리스트안에 리스트로 간선 정보 받기

# 이동할 네 방향(상, 하, 좌, 우)정의
dx = [-1, 1, 0, 0] # dx 정의(좌 우)
dy = [0, 0, -1, 1] # dy 정의(상 하)

index = 2 # BFS 돌리고 나서 값을 바꿔주려고.
cnt = [] # cnt들을 담을 리스트.
res = 0 # 단지의 개수
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j, index)) # bfs 돌려서 cnt값을 append
            index += 1 # 인덱스 하나씩 증가시키면서 바꿔주는거
            res += 1 # 단지의 개수 하나씩 증가.

cnt.sort() # 오름차순 정렬
print(res) # 단지의개수
for c in cnt:
    print(c) # 단지내 집의 개수를 오름차순으로 프린트.