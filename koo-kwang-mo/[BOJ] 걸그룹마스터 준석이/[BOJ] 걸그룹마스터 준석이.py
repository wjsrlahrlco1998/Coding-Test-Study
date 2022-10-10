N, M = map(int,input().split())
glgp={}
result=[]
for i in range(N):
    tmp=input()
    tmp2=[]
    for j in range(int(input())):
        tmp2.append(input())
    tmp2=sorted(tmp2)
    for j in tmp2:
        glgp[j]=tmp
for i in range(M):
    tmp=input()
    quiz=int(input())
    if quiz==0:
        for name,group in glgp.items():
            if tmp==group:
                result.append(name)
    elif quiz==1:
        result.append(glgp.get(tmp))
for j in result:
    print(j)