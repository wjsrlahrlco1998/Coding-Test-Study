import math

def convert_time(times):
    '''시간:분 형식을 분으로 변환하는 함수'''
    times = list(map(int, times.split(":")))
    convert_minutes = times[0] * 60 + times[1]
    return convert_minutes

def cal_fee(sum_time, basic_minutes, basic_fee, std_minutes, std_fee):
    '''누적 주차 시간(분)으로 주차요금을 계산하는 함수'''
    if sum_time - basic_minutes <= 0:
        return basic_fee
    else:
        sum_time = sum_time - basic_minutes
        return basic_fee + math.ceil(sum_time / std_minutes) * std_fee

def solution(fees, records):
    answer = []

    # 1. 요금 변수 정의
    basic_minutes = fees[0]         # 기본 시간(분)
    basic_fee = fees[1]             # 기본 요금(원)
    std_minutes = fees[2]           # 단위 시간(분)
    std_fee = fees[3]               # 단위 요금(원)

    # 2. 자동차별 주차정보를 저장할 dict 자료형 정의
    dict_records = dict()

    # 3. 자동차별 누적 주차 시간(분) 계산
    for record in records:
        # 1) 정보를 공백을 기준으로 나누기(시각, 차량번호, 내역 순)
        record = record.split()

        # 2) 차량 상태 저장(입차 or 출차)
        status = record[2]

        # 3) 주차정보에 해당 차량번호가 없는 경우 새로 만들기
        if record[1] not in dict_records:
            dict_record = dict()
            dict_record["IN"] = -1
            dict_record["OUT"] = 0
            dict_record["SUM"] = 0
            dict_record["fee"] = 0
            dict_records[f"{record[1]}"] = dict_record

        # 4) 주차 상태별 누적 주차 시간 계산
        if status == "IN":
            dict_records[f"{record[1]}"]["IN"] = convert_time(record[0])
        else:
            dict_records[f"{record[1]}"]["OUT"] = convert_time(record[0])
            dict_records[f"{record[1]}"]["SUM"] += abs(dict_records[f"{record[1]}"]["OUT"] - dict_records[f"{record[1]}"]["IN"])
            dict_records[f"{record[1]}"]["IN"] = -1
            dict_records[f"{record[1]}"]["OUT"] = 0
    
    # 4. 출차 기록이 없는 자동차의 누적 주차 시간 계산(23:59 출차로 가정)
    for car_num, car_info in dict_records.items():
        if car_info["IN"] != -1:
            car_info["SUM"] += abs(convert_time("23:59") - car_info["IN"])
            dict_records[f"{car_num}"]["IN"] = 0
            dict_records[f"{car_num}"]["SUM"] = car_info["SUM"]
    # 5. 주차요금 계산
    for car_num, car_info in dict_records.items():
        car_info["fee"] = cal_fee(car_info["SUM"], basic_minutes, basic_fee, std_minutes, std_fee)
        dict_records[f"{car_num}"]["fee"] = car_info["fee"]
    
    # 6. 차량 번호순 별로 정렬
    dict_records = sorted(dict_records.items(), key = lambda x : x[0])
    answer = [record[1]["fee"] for record in dict_records]

    return answer