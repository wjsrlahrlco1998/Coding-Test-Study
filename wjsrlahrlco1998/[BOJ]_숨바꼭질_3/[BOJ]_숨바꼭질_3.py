import sys
import heapq

# 1. 수빈 위치 (N), 동생 위치 (K) 입력 : 0 <= N, K <= 100,000
N, K = map(int, sys.stdin.readline().split())

if N <= K:
    n = K
else:
    n = N

# 2. 그래프의 정보 입력
INF = int(1e9)                                              # 무한대 정의 : 연결되지 않은 경우
graph = [[] for _ in range(n * 2 + 1)]                          # 정점을 N + 1까지로 정의 : X * 2만큼 이동 후 -1만큼 하는 경우

for i in range(n + 1):

    # 걷는 경우의 이어진 노드와 거리(시간)
    graph[i].append((i + 1, 1))                             # i -> i + 1 사이의 걷는 거리(시간) : 1
    graph[i + 1].append((i, 1))                             # i + 1 -> i 사이의 걷는 거리(시간) : 1
    
    # 순간이동하는 경우의 이어진 노드와 거리(시간)
    graph[i].append((i * 2, 0))                             # i -> i * 2 사이의 걷는 거리(시간) : 0

# 3. 최단거리 테이블
distance = [INF for _ in range((n * 2) + 1)]

# 4. 다익스트라 함수 정의
def dijkstra(start):
    distance[start] = 0                                     # 자기자신과의 거리는 0으로 초기화

    pq = []
    heapq.heappush(pq, (0, start))                          # start -> start로 가는 정보 (거리 : 0, 도착지점 : start) push

    # 1) 더 이상 갈 곳이 없을 때까지 반복
    while pq:
        # (1) 현재 노드로의 거리와 현재 노드 위치
        dist, now = heapq.heappop(pq)

        # (2) 현재 노드로의 거리 정보가 이미 업데이트 되었다면 continue
        if distance[now] < dist:
            continue
            
        # (3) 현재 노드(now)와 인접한 노드를 확인하여 가중치 갱신
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))

# 5. 다익스트라 함수 실행
dijkstra(N)

# 6. 결과
print(distance[K])