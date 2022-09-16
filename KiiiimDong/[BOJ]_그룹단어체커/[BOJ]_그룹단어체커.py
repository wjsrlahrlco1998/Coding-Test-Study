import sys
input = sys.stdin.readline
n = int(input())
cnt = 0    
for i in range(n):
    word = input()
    group_word = []    
    for s in word:
        if s in group_word:
            if group_word[-1] != s:
                break
        else:
            group_word.append(s)
    else: # for ~ else : for문에서 break가 동작하지 않을 때 동작.
        cnt += 1
print(cnt)