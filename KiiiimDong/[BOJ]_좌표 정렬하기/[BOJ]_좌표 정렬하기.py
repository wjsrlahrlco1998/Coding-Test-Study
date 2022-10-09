# 1. 입력값 받기
n = int(input()) # 점 개수 n
xy_list = [] # x,y를 받을 리스트

# 2. x,y 입력받기
for i in range(n):
    x, y = map(int, input().split(' ')) # x, y를 int로 받아준다.
    xy_list.append([x,y]) # x,y를 [x,y] 리스트 형태로 xy_list안에 넣어준다.

# 3. key값 이용해서 정렬하기
xy_list.sort(key = lambda x: (x[0], x[1])) # x[0]을 기준으로 오름차순 한번, x[1]기준으로 오름차순 한번 정렬

# 4. 정렬된 x,y를 출력하기
for i in range(n):
    print(xy_list[i][0], xy_list[i][1]) # 앞에 들어간애가 x, 뒤에가 y라서 이렇게 출력.