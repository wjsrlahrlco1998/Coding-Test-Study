N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
####

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
#2차원 배열 graph에 n번째 인덱스에는 n과 촌수관계로 맺어진 숫자들이 저장됨.
'''print(graph)
예제 1의 출력
[[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
'''
# dfs
def dfs(v, num):
  num += 1#촌수
  visited[v] = True#방문체크

  if v == B:#dfs 최종 도달하면
    result.append(num)#값 반환

  for i in graph[v]:#A와 n촌 관계인 사람 중에서 1촌으로 묶인 사람들을 조사한다.
    if not visited[i]:#조사하지 않은 사람들에 대해서 DFS 다시 진행
      dfs(i, num)#재귀함수를 통해 B를 찾아간다.

dfs(A, 0)
if len(result) == 0:#없으면 0
  print(-1)
else:
  print(result[0]-1)

#출처 https://wonyoung2257.tistory.com/56
