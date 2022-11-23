from collections import deque#BFS 활용을 위한 덱
import sys#input 대신 read를 사용하기 위함, read가 시간이 더 적게든다.
read = sys.stdin.readline#read를 선언함으로써 input대신에 read 사용.

N, M, K = map(int, read().split())#인자 받아오기
graph = [[0] * (N + 1) for _ in range(N + 1)]#각 숫자들의 관계를 담을 2차원 리스트
for i in range(M):#관계도 받아오기
    a, b = map(int,read().split())#관계가 있는 두 숫자를 받은 후
    graph[a][b] = graph[b][a] = 1#a <-> b 양 방향에서 확인 가능하도록 입력한다.

visited = [0] * (N+1)#중복 확인을 방지할 수 있는 리스트
visited2 = [0] * (N+1)


def BFS(x):
    q = deque()#덱을 부름.
    q.append(x)#덱의 초기값 추가
    visited[x] = 1#초기값의 방문기록
    while q:#덱의 내용물이 있을 경우 계속 반복
        x = q.popleft()#가장 오래된 값을 먼저 불러옴.
        print(x, end = " ")#예제 출력에 알맞은 출력형식
        for i in range(1, N + 1):#정점이 같은 수준이라면 작은 수 먼저 체크함으로 1~N까지 오름차순으로 탐색.
            if visited[i] == 0 and graph[x][i] == 1:#방문한 적이 없고, x와 연결된 i를 고른다.
                q.append(i)#덱에 추가하고
                visited[i] = 1#방문 기록.


def dfs(x):#DFS
    visited2[x] = 1#재귀함수로 호출됨으로 함수를 실행하자 마자 방문 기록
    print(x, end=" ")#출력
    for i in range(1, N + 1):#작은 수 부터 체크함으로 1~N
        if visited2[i] == 0 and graph[x][i] == 1:#방문 X, x와 i가 연결된 경우.
            dfs(i)#연결된 i에서 재귀함수 호출
dfs(K)
print()
BFS(K)