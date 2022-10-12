import sys
from collections import deque

read = sys.stdin.readline

# 1. 상자의 크기 입력 받기 : M(가로) X N(세로) : 2 <= N, M <= 1000
M, N = map(int, input().split())

# 2. 상자정보 입력 받기
box_info = []

for _ in range(N):
    box_info.append(list(map(int, input().split())))

# 3. BFS
def bfs(x, y, queue):
    
    # 1) 상하좌우 이동 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if box_info[nx][ny] != 0:
            continue

        if box_info[nx][ny] == 0:
            box_info[nx][ny] = 1
            queue.append((nx, ny))
    

# 4. 일수를 저장할 변수와 토마토가 있는 좌표를 담을 큐 정의
days = 0
queue = deque()     # 그 당시 돌아야할 시작점만 저장할 큐
r_queue = deque()   # 새로운 시작점을 저장할 큐

# 1) 토마토가 있는 좌표 담기
for i in range(N):
    for j in range(M):
        if box_info[i][j] == 1:
            r_queue.append((i, j))


while r_queue:
    queue = r_queue.copy()
    r_queue = deque()
    while queue:
        x, y = queue.popleft()
        bfs(x, y, queue=r_queue)
        
        # 중복좌표 제거 --> 시간초과가 발생하므로 삭제
        # r_queue = set(r_queue)
        # r_queue = deque(r_queue)
    days += 1   

# 5. 익지않은 토마토가 있으면 -1, 아니면 최소일수 출력
for i in box_info:
    if 0 in i:
        print(-1)
        break
else:
    print(days - 1)