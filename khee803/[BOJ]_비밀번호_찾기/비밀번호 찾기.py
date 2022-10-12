N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, pw = input().split()
    dic[site] = pw

for _ in range(M):
    print(dic[input()])