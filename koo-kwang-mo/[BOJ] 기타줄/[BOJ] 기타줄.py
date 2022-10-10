n, m = map(int,input().split())
list_package = []
list_single = []
result = []
for i in range(m):
    package, single = map(int,input().split())
    list_package.append(package)
    list_single.append(single)

result.append(n*min(list_single))
result.append((n//6 + 1)*min(list_package))
x = min(list_single)*(n%6) + min(list_package)*(n//6)
result.append(x)
print(min(result))