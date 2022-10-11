from collections import Counter
N = int(input())
list = []
for _ in range(N):
    name, ex = input().split('.')
    list.append(ex)

cnt = Counter(list).most_common()
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i][0], cnt[i][1])