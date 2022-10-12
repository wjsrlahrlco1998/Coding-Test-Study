m,n = map(int,input().split())
l1 = []
for i in range(m+n):
    p = input()
    l1.append(p)

dup = {x for x in l1 if l1.count(x) > 1}
print(len(dup))
for i in sorted(dup):
    print(i)