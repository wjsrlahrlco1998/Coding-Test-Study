import heapq
import sys

# 1. 정점의 개수(V)와 간선의 개수(E) 입력받기 : 1 <= V <= 20000, 1 <= E <= 300000
V, E = map(int, sys.stdin.readline().split())

# 2. 시작 정점 (K) 입력 : 1 <= K <= V
K = int(sys.stdin.readline())

# 3. 그래프 정의
INF = int(1e9)                                              # 무한대 정의
graph = [[] for _ in range(V + 1)]                          # 그래프 정의

# 4. 최단거리 테이블 정의
distance = [INF for _ in range(V + 1)]

# 5. 간선 정보 입력받기
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())        # u -> v로 가는 비용 w
    graph[u].append((v, w))

# 6. 다익스트라
def dijkstra(start):
    distance[start] = 0                                     # 자기 자신에게 가는 거리는 0으로 초기화

    # 1) 최소 힙 정의
    pq = []
    heapq.heappush(pq, (0, start))                          # 최소 힙에 push (자기자신에게 가는거리)

    # 2) 
    while pq:
        # (1) 가장 거리가 짧은 노드의 정보 pop
        dist, now = heapq.heappop(pq)

        # (2) 해당 노드(now)가 이미 처리된 적이 있는 노드이면 continue
        if distance[now] < dist:
            continue

        # (3) 현재 노드(now)와 인접한 노드를 확인하여 가중치 갱신
        for node in graph[now]:
            cost = dist + node[1]                           # cost : 현재 노드(now) 까지의 거리 + now에서 인접한 node까지의 거리
            if cost < distance[node[0]]:                    # 위의 cost가 최단거리 테이블에 정의된 거리보다 짧다면 갱신
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))         # 최소 힙에 갱신된 정보를 push

# 7. 다익스트라 실행
dijkstra(K)

# 8. 결과 출력
for i in range(1, V + 1):
    # 1) 도달할 수 없는 경우
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])