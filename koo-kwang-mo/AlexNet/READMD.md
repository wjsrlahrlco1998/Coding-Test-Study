# AlexNet

LeNet과 비교해 최근에 발표되었다. LeNet과 유사하지만 다른 점이 존재한다.

구조

<img src = '그림1.JPG'>

## 활성화 함수

ReLU를 이용한다.

## LeNET과의 차이점

 1) 활성화 함수로 ReLU를 이용한다.
 2) LRN(local response normalization)이라는 국소적 정규화를 실시하는 계층을 이용한다.
 3) 드롭아웃을 이용한다.


## 드롭 아웃이란??

<img src = '그림2.JPG'>

오버피팅을 방지하기 위하여 계층의 뉴런을 임의 삭제한다.
이 때 삭제한 비율을 곱하여 결과를 출력한다.

