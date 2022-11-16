from collections import deque 
import sys
input = sys.stdin.readline

def bfs(graph,x,y,index):
    queue = deque()
    queue.append((x,y)) # 큐에 x,y append
    while queue: # 큐가 빌때까지
        x, y = queue.popleft() # 큐에서 x, y좌표 꺼냄

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny <0 or ny >=M:# 땅 벗어나면 무시
                continue

            if graph[nx][ny] == 0:# 0일때도 무시
                continue

            if graph[nx][ny] == 1: # 1일때만
                graph[nx][ny] = index # 2로 초기화 시켜준다.
                queue.append((nx,ny)) # 변경된 좌표 append      

T = int(input()) # 테스트 케이스 수

# 상, 하, 좌, 우 설정
dx = [-1,1,0,0]
dy = [0, 0, -1,1]

for i in range(T):
    M,N,K = map(int,input().split()) # 가로, 세로, 배추개수
    graph = [[0 for p in range(M)]for q in range(N)] # M * N 그래프
    
    index = 2
    cnt = 0
    for j in range(K):
        v,w = map(int,input().split()) # 배추 있는 좌표
        graph[w][v] = 1  # 1로 초기화(배추 있는 지점의 graph 값 1로 설정)   

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1: # 배추 있는 지점이면
                    bfs(graph,a,b,index) # bfs 돌려서
                    cnt += 1 # bfs 돌릴때마다 count
    print(cnt) # bfs 돌린횟수 카운트.