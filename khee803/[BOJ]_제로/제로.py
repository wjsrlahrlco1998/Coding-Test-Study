K = int(input())
list = []
for _ in range(K):
    num = int(input())
    if num != 0:
        list.append(num)
    else:
        list.pop()
print(sum(list))