import matplotlib.pyplot as plt
import numpy as np


data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

x_data = np.array(x)
y_data = np.array(y)

a = 0
b = 0 #학습 이전 0으로 초기화

lr = 0.05 # 학습률

epochs = 2000#반복횟수

#경사하강법

for i in range(epochs):
    y_pred = a * x_data + b#predict함수가 아니라 직선함수 y= ax + b 형태로 예측
    error = y_data - y_pred#오차 : 결과 - 예측

    a_diff = -(1 / len(x_data)) * sum(x_data * (error))#평균 제곱 오차를 a로 비분한 값
    #         =  2/n, 2가 1이 되는 과정은 단순히 계산간편, y^ = ax+b, error = y^ - y
    #다시말해 x*(y^ - y) = x*error가 된것이다.
    b_diff = -(1 / len(x_data)) * sum(y_data - y_pred)# 평균 제곱 오차를 b로 미분한 값 ---------------******이해 어려움
    # 어려웠던 점 : 편미분, 편미분을 수식화 한 것.
    # 꼭 다시 한 번 리마인드 하기. README의 그림4, 와 함께 이해할 것


    a = a - lr*a_diff#학습률 * 미분결과 후 기존 a값 업데이트
    b = b - lr*b_diff#업데이트

    if i%100 == 0: #epoch가 100번 될 때 마다 출력
        print("epoch = %.f, 기울기 = %.04f, 절편 = %.04f, 에러 = %.04f" % (i, a, b, error.mean()))

plt.scatter(x,y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()