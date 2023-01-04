### 1. 퍼셉트론의 활성화 함수로 계단 함수를 사용할 수 있다.

#### 1) 단순 구현

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

x 실수만 받아드릴 수 있기 때문에 넘파이 배열을 입력할 수는 없다.

##### a.넘파이 대입

import numpy as np
x = np.array([-1.0, 1.0, 2.0])

y = x > 0 #x 각 인덱스의 값이 0을 넘는지 안 넘는지에 대한 불 값을 저장한다.

y의 출력
array([Fasle, True, True])

y = y.astype(np.int) #불 값을 int형으로 바꾼다.
y의 출력
array([0, 1, 1])

