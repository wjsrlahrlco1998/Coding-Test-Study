n = input() # n 문자열로 받아주기
m = sorted(n)[::-1] # 오름차순 정렬한거를 내림차순으로 바꿈
print(''.join(m)) # join으로 리스트-> 다시 문자열로 바꿔줌. 
