l = [int(input()) for i in range(9)]
a=0
index=0
for i in range (len(l)):   
    if l[i]>a:
        a=l[i]
        index=i+1
    else:
        a=a
print(a)
print(index)