S = input() # 1. 전체 단어
Alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 2. 붙어나오는 특수케이스들 정리한 리스트

for i in Alphabet_list: # 3. 붙어서 나오는 애들 하나씩 꺼내는거
    S = S.replace(i, ' ') # 4. 붙어서 나오는 애들을 공백으로 치환(공백은 한칸이므로 len(s)로 세면 한 알파벳으로 취급)

print(len(S)) # 5. 알파벳의 개수