x = int(input()) # 목표숫자 x
stick = [64] # stick의 초기 길이 64

while sum(stick) > x: # stick길이가 x보다 클때만 작동.
    short = stick.pop() # stick의 제일 작은 부분 꺼냄.
    stick.append(int(short / 2)) # 제일 작은 길이를 절반으로 자른거 두번 append
    stick.append(int(short / 2))
    if sum(stick[0:len(stick)-1]) >= x: # 절반으로 자른거 두개중 하나를 버린값이 x보다 크다면   
        stick.pop() # 하나를 버린다.
print(len(stick)) # stick의 길이를 출력한다.
