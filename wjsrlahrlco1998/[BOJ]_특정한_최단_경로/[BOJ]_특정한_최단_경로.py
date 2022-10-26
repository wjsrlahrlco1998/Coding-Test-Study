import heapq
import sys

# 1. 정점의 개수(N)과 간선의 개수(E) 입력 : 2 <= N <= 800, 0 <= E <= 200,000
N, E = map(int, sys.stdin.readline().split())

# 2. 그래프 정보 입력
INF = int(1e9)                                          # 무한대 정의 : 간선이 없는 경우(INF)
graph = [[] for _ in range(N + 1)]                      # 그래프

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))

# 3. 반드시 거쳐야하는 서로 다른 정점 v1, v2 입력
v1, v2 = map(int, sys.stdin.readline().split())

# 4. 다익스트라 함수 정의
def dijkstra(start = 1):
    distance = [INF for _ in range(N + 1)]              # 최단거리 정보를 저장할 테이블
    distance[start] = 0                                 # 자기자신에 대한 거리는 0으로 초기화

    pq = []                                             # 힙으로 사용할 리스트 선언
    heapq.heappush(pq, (0, start))                      # start -> start로 가는 정보 (거리 : 0, 도착지점 : start) push

    # 1) 더 이상 갈 곳이 없을 때까지 반복
    while pq:
        # (1) 현재 가장 거리가 짧은 노드 정보 pop -> 현재 나의 위치
        dist, now = heapq.heappop(pq)

        # (2) 해당 노드(now)가 이미 처리된 적 있다면 continue
        if distance[now] < dist:
            continue

        # (3) 현재 노드(now)와 인접한 노드를 확인하여 가중치 갱신
        for node in graph[now]:
            cost = dist + node[1]                       # cost : 현재 노드(now) 까지의 거리 + 현재 노드(now)에서 인접한 node까지의 거리
            if cost < distance[node[0]]:                # cost가 현재 최단 거리 테이블 상의 거리보다 짧다면 갱신
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))     # now -> node[0]까지 가는 거리(갱신된 거리)를 최소 힙에 push
    
    return distance

# 5. 최단거리 구하기
# 1) 각 시작정점 별 최단거리
start_dist = dijkstra(start=1)                          # 1 -> N까지의 최단거리
v1_dist = dijkstra(start=v1)                            # v1 -> N까지의 최단거리
v2_dist = dijkstra(start=v2)                            # v2 -> N까지의 최단거리

# 2) v1과 v2를 지나는 경로 중 최단거리
target = min(start_dist[v1] + v1_dist[v2] + v2_dist[N],
            start_dist[v2] + v2_dist[v1] + v1_dist[N])  # start -> v1 -> v2 -> N과 start -> v2 -> v1 -> N 중 최단거리 구하기

# 6. 결과
if target >= INF:                                       # 경로가 없는 경우
    print(-1)
else:                                                   # 경로가 존재하는 경우
    print(target)