def solution(s):
    # 1. 문자열 s를 소문자로 만든다.
    s = s.lower()

    # 2. 문자열 s를 공백을 기준으로 분리한다.
    input_str_list = s.split(" ")

    # 3. 결과를 저장할 리스트를 초기화한다.
    output_str_list = []

    # 4. JadenCase 문자열 변환
    for word in input_str_list:
        # 1) 한 단어의 길이가 1보다 큰 경우 : 첫글자만 대문자를 변환하고 뒤에는 이어 붙인다.
        if len(word) > 1:
            word = word[0].upper() + word[1:]
            output_str_list.append(word)
        # 2) 한 단어의 길이가 1보다 작은 경우 : 바로 대문자로 변환한다.
        else:
            word = word.upper()
            output_str_list.append(word)

    # 5. 결과를 저장한 리스트를 공백을 두고 조인한다.
    answer = " ".join(output_str_list)
    return answer