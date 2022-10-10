m,n = map(int,input().split())

a = set()
for i in range(m):
    a.add(input())
b = set()
for i in range(n):
    b.add(input())

result = sorted(list(a&b))

print(len(result))
for i in result:
    print(i)