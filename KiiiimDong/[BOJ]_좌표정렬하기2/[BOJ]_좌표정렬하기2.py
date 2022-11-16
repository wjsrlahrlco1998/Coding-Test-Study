n = int(input()) # 점개수 n

sort_list = [] # x,y 좌표 받아줄 리스트
for i in range(n):
    a, b = map(int, input().split()) # x,y 좌표
    sort_list.append([a, b]) # 리스트로 넣어줘야
sort_list.sort(key = lambda x: (x[1], x[0])) # 이렇게 인덱스로 불러와서 정렬가능.

for i in range(n):
    print(sort_list[i][0], sort_list[i][1]) # x, y 출력 