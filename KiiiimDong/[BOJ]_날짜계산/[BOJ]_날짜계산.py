e, s, m = map(int, input().split()) # e, s, m (15, 28, 19의 주기)

year = 1 # 1년부터.

while True:
    if (year-e) % 15 == 0 and (year-s) % 28 == 0  and (year-m) % 19 == 0: # (year-년도)/주기 를 해서 모두 0이 되면
        break # break 걸어준다.
    year += 1 # year를 1씩 늘려주면서 계속해서 비교해본다.

print(year) # break 걸렸을때 year를 출력.