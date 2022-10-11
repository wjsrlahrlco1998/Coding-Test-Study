import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(N):
    pokemon = sys.stdin.readline().strip()
    dic[i+1] = pokemon

r_dic = {v:k for k,v in dic.items()} #key,value 뒤집은 딕셔너리

for i in range(M):
    x = sys.stdin.readline().strip()
    if x.isdigit() == True:
        print(dic[int(x)])
    else:
        print(r_dic[x])