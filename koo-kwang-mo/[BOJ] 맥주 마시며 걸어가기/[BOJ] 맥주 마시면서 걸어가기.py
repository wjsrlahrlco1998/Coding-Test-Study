from collections import deque

def bfs():
    q = deque()
    q.append((home_x,home_y))
    while q:
        x,y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print('happy')
            return
        for i in range(n): #편의점들 확인
            if not visited[i]: #편의점을 방문하지 않았다면
                new_x,new_y = graph[i] #편의점의 좌표를 새로 뽑고
                if abs(x-new_x) + abs(y-new_y) <= 1000: #다음거리까지 갈 수 있다면
                    visited[i] = 1 #방문체크해주고
                    q.append((new_x,new_y)) #큐에 담아준다
    print('sad')
    return
#1번째 반복에서는 집 -> 편의점을 확인한다
#다음 편의점까지의 거리가 1000 이하면은 -> 50미터에 한병/ 20병의 거리
#1000이하면 다음 편의점까지 무사히 갈 수 있다는 것

t = int(input())
for _ in range(t):
    n = int(input())
    home_x,home_y = map(int,input().split())
    graph = []
    for _ in range(n):
        x,y = map(int,input().split())
        graph.append((x,y))
    festival_x,festival_y = map(int,input().split())
    visited = [0 for _ in range(n+1)]
    bfs()