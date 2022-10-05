N = int(input())
L = []
list_n = []
for i in range(N):
    w, h = input().split()
    list = [w, h]
    L.append(list)
for i in range(N):
    list_n.append(1)#초기 모든 사람의 덩치 순위는 1이다.

def com(x,y):#덩치 비교 함수, 덩치가 작은 사람 반환하며 비교가 안되면 0을 반환.
    if int(x[0]) < int(y[0]):
        light = x
    else :
        light = 0
    if int(x[1]) < int(y[1]):
        short = x
    else :
        short = 0
    if light == short:
        result = light
    else:
        result = 0
    return result

for i in range(N):#모든 사례에 대해서 전수조사.
    for j in range(N):
        if com(L[i], L[j]) == L[i]:
            list_n[i] += 1
for i in range(N):
    print(list_n[i],end=' ')
