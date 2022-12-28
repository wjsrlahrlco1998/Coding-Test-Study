n = int(input()) # 학생의 수
numbers = [] # 학생들의 번호를 받아줄 리스트.
for i in range(n):
    numbers.append(input()) # 학생들의 번호를 학생수만큼 받아준다.

k = 1 # k는 1부터 시작(1개부터~n개까지 해야하니깐)
while True:
    if len(set(map(lambda x: x[-k:], numbers))) == n: # 뒤에서부터 k개 뜯어내고 중복제거해도 중복이 제거가 안될때(n개가 그대로 있을때)
        print(k) # k값을 출력한다.
        break 
    k += 1 # 중복이 없을 때까지 계속 k를 늘려가는 방식(뒤에서부터 뜯어내는 개수)

