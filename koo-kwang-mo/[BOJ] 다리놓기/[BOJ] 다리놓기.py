def factorial(x):
    n=1
    for i in range(1,x+1):
        n = n*i
    return n

N = int(input())
n_list=[]
for i in range(N):
    n1,n2 = input().split()
    list =[n1, n2]
    n_list.append(list)
result = []
for i in range(N):

    x = int(n_list[i][1])
    y = int(n_list[i][0])
    z = x-y
    output = factorial(x)/(factorial(y)*factorial(z))
    print(int(output))
    #result.append(output)
