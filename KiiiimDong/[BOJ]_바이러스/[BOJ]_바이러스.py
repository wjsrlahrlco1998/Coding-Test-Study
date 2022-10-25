from collections import deque
import sys
input = sys.stdin.readline
n= int(input()) # 정점의 개수
m= int(input()) # 간선의 개수

graph = [[] for _ in range(n+1)] # graph를 정점의 개수만큼 초기화(이차원리스트로)
for _ in range(m): # 간선의 개수만큼반복
    a, b = map(int, input().split()) # 정점 연결관계 받아줌
    # 양방향 간선이니깐 양방향으로 다 append
    graph[a].append(b)
    graph[b].append(a)
    

# 정점 낮은번호부터 먼저 방문해야 하니깐 오름차순으로 정렬
for i in range(1, n+1):
    graph[i].sort()

def bfs(graph, v, visited): # graph(이차원리스트), 시작점, 방문처리여부리스트
    queue = deque([v]) # 덱으로 큐를 구현한다.
    visited[v] = True
    global cnt # global변수로 선언
    
    while queue: # 큐가 빌 때까지 반복
        now = queue.popleft() # 큐에서 하나의 원소를 뽑아서 출력
        cnt += 1

        for i in graph[now]: # 해당 원소와 연결된것들중에서
            if not visited[i]: # 방문하지 않은 원소들을
                queue.append(i) # 큐에 삽입
                visited[i] = True # 방문처리

visited = [False] * (n+1) # visited False로 초기화 
cnt = 0 # cnt 초기화
bfs(graph, 1, visited) # 그래프, 시작점, visited리스트
print(cnt-1) # 첫 popleft()는 처음 들어간 정점인데 그것까지 세게 되기때문에 그걸 하나 빼준다.