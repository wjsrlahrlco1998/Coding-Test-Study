import sys
from collections import deque

read = sys.stdin.readline

# 1. 미로 크기 입력받기 : N >= 2, 2 <= M <= 100인 정수
N, M = map(int, input().split())

# 2. 미로 구조 입력받기
maze = []

for i in range(N):
    maze.append(list(map(int, input())))

# 3. BFS
'''
# 미로 상태 출력
def print_maze(maze):
    for i in range(len(maze)):
        print(maze[i])
    print("=" * 15)
'''

def bfs(x, y):
    # 1) 상하좌우 이동 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 2) 이동 좌표를 담을 큐 정의
    queue = deque()
    queue.append((x, y))

    # 3) 인접한 노드 위주로 모든 좌표를 돌아보자(BFS) // 더 이상 갈 수 있는 좌표가 없을 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # (1) 모든 좌표를 돌아본다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 미로의 범위를 넘어가면 X
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 이동하려는 좌표가 0 즉, 막혀있으면 X
            if maze[nx][ny] == 0:
                continue
            
            # 이동하려는 좌표가 1이면 진행 O
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1   # 이동한 좌표에 지금까지 거쳐온 횟수 + 1
                queue.append((nx, ny))          # 이동한 좌표를 큐에 넣어준다.
    
            # print_maze(maze) : 형상 출력
    return maze[N-1][M-1]

print(bfs(0, 0))
        