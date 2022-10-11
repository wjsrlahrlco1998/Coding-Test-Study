N, M = map(int, input().split())

a = set(input() for _ in range(N))
b = set(input() for _ in range(M))

result = sorted(list(a & b))
print(len(result))
for i in result:
    print(i)