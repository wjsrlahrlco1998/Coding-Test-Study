import sys
from collections import deque

input = sys.stdin.readline


def bfs(M, N, box):
    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1 # 처음에 들어오자마자 다 익어있을 때 0 을 출력해야하니깐 시작할 때 +1 되는거 고려해서 -1 부터 시작.

    while ripe: # 큐가 빌 때까지
        days += 1
        for _ in range(len(ripe)): 
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i] # 상하좌우
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0): # 범위(m X n)안에 들어오고, 토마토가 익지 않았을 때(box값이 0) 
                    box[nx][ny] = box[x][y] + 1 # 토마토를 익은것으로 바꿔준다.
                    ripe.append([nx, ny]) # 진행한 곳의 좌표를 다시 넣어준다.

    for b in box:
        if 0 in b: # 다 익지 못할 때 -1
            return -1
    return days # 다 익을수 있을 때 몇일인지 출력


M, N = map(int, input().split()) # m x n 
box = [] # box 그래프(토마토를 담을 그래프)
ripe = deque() # 큐를 구현

for i in range(N):
    row = list(map(int, input().split())) # 토마토가 들어있는 상태, 익은상태, 들어있지 않은 상태를 받아준다.(-1,0,1)
    for j in range(M): # 가로만큼
        if row[j] == 1: #  j(행) row(열)
            ripe.append([i, j]) # 익어있으면 몇행 몇열인지 append
    box.append(row) # 그냥 그래프 정보를 다 넣어주는거  


print(bfs(M, N, box)) # bfs돌려서 return 값 출력