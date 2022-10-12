m,n = map(int,input().split())
l1 = []
for i in range(m+n):
    p = input()
    l1.append(p)

dup = {x for x in l1 if l1.count(x) > 1}
print(len(dup))
for i in sorted(dup):
    print(i)
#리스트를 사용하면 시간복잡도가 커진다. set은 아님 /set 인덱스 번호가 아닌 해쉬테이블로 찾기 떄문에 빠르다.