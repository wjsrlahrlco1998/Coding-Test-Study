import sys
from collections import deque

read = sys.stdin.readline

# 1. 컴퓨터의 개수 입력
n_cum = int(input())

# 2. 연결되어있는 컴퓨터 쌍의 수
n_net = int(input())

# 3. network 정보 입력
network = [[0] * (n_cum + 1) for _ in range(n_cum + 1)]

for _ in range(n_net):
    a, b = map(int, input().split())
    network[a][b] = 1
    network[b][a] = 1


# 4. 방문확인을 위한 리스트 선언
visited = [0] * (n_cum + 1)

# 5. 탐색(BFS)
def bfs(v=1):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    cnt = 0

    while queue:
        x = queue.popleft()
        for i in range(1, n_cum + 1):
            if (network[x][i] == 1) and (visited[i] == 0):  # 가고자하는 노드와 이어져있고, 방문하지 않았던 노드라면 방문한다.
                visited[i] = 1
                queue.append(i)
                cnt += 1
    
    return cnt

# 6. 결과
print(bfs())