from collections import deque # 덱 불러옴(BFS에 이용)
import sys
input = sys.stdin.readline

# DFS
def dfs(graph, v, visited): # graph(이차원리스트), 시작점, 방문처리여부리스트
    
    visited[v] = True # 현재 노드를 방문처리
    print(v, end=' ') # v를 출력하는데, 띄어쓰기를 해주면서 출력한다.
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 방문하지않은 노드에대해서
            dfs(graph, i, visited) # dfs를 재귀적으로 실행시킨다.

def bfs(graph, v, visited): # graph(이차원리스트), 시작점, 방문처리여부리스트
    queue = deque([v]) # 덱으로 큐를 구현한다.
    visited[v] = True

    while queue: # 큐가 빌 때까지 반복
        now = queue.popleft() # 큐에서 하나의 원소를 뽑아서 출력
        print(now, end=' ')

        for i in graph[now]: # 해당 원소와 연결된것들중에서
            if not visited[i]: # 방문하지 않은 원소들을
                queue.append(i) # 큐에 삽입
                visited[i] = True # 방문처리


n, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색시작번호
graph = [[] for _ in range(n+1)] # graph를 정점의 개수만큼 초기화(이차원리스트로)
for _ in range(m): # 간선의 개수만큼반복
    a, b = map(int, input().split()) # 정점 연결관계 받아줌
    # 양방향 간선이니깐 양방향으로 다 append
    graph[a].append(b)
    graph[b].append(a)

# 정점 낮은번호부터 먼저 방문해야 하니깐 오름차순으로 정렬
for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n+1) # 방문을 다 false로 초기화
dfs(graph, v, visited) # 그래프, v(처음 출발지점), visited(다 false로 초기화 되어있는)
print() # 중간에 개행해줘야해서
visited = [False] * (n+1) # 방문을 다 false로 초기화
bfs(graph, v, visited) # 그래프, v(처음 출발지점), visited(다 false로 초기화 되어있는)