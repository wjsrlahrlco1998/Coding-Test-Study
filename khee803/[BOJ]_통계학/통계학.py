import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

#산술평균
print(int(round(sum(nums)/N)))

#중앙값
print(sorted(nums)[N//2])

#최빈값
cnt = Counter(nums).most_common()
cnt.sort()
cnt.sort(key=lambda x:x[1], reverse=True)
if len(cnt) == 1: 
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]: #최빈값 2개 이상
    print(cnt[1][0])
else:
    print(cnt[0][0])

#범위
print(max(nums)-min(nums))