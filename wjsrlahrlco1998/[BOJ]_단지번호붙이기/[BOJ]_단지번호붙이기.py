import sys
from collections import deque

read = sys.stdin.readline

# 1. 지도의 크기 입력 : 5 <= N <= 25
map_size = int(input())

# 2. 단지 정보 입력
apt_info = []

for _ in range(map_size):
    apt_info.append(list(map(int, input())))

# 3. BFS 함수 정의
def bfs(x, y):
    # 1) 상하좌우 이동정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 2) 이동좌표를 담을 큐 정의
    queue = deque()
    queue.append((x, y))

    apt_info[x][y] = 2

    # 3) 집의 수 카운트
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size:
                continue

            if apt_info[nx][ny] != 1:
                continue
            
            if apt_info[nx][ny] == 1:
                apt_info[nx][ny] = 2
                count += 1
                queue.append((nx, ny))
    
    return count


# 4. 단지내 집의 수를 저장할 리스트
n_houses = []   # 단지내 집의 수
n_apts = 0  # 단지의 수

for i in range(map_size):
    for j in range(map_size):
        if apt_info[i][j] == 1:     # 방문하지 않고, 집이 있는 경우
            n_houses.append(bfs(i, j))
            n_apts += 1

# 5. 단지내 집의 수 오름차순 정렬
n_houses.sort()

# 6. 결과 출력
print(n_apts)
for n in n_houses:
    print(n)

# 7. 방문 후 행렬 확인
'''for i in range(len(apt_info)):
    print(apt_info[i])'''