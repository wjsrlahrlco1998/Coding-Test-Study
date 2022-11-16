import sys
n = int(sys.stdin.readline()) #정해진 개수의 정수를 한줄에 입력(input()보다 시간절약)
data = list(map(int,sys.stdin.readline().split())) #임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때 사용
s_data = list(sorted(set(data))) #set으로 중복 x

dic = {s_data[i]:i for i in range (len(s_data))}

for i in data:
    print(dic[i],end=' ')