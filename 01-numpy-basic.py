# -*- coding: utf-8 -*- 

import numpy as np
# numpy 다차원 배열을 다루는 패키지

# vector = 행(세로), matrix = = 열(가로), Tensor=3차원

list_data = [1,2,3]
array = np.array(list_data)

print(array.size)
# 데이터  사이즈
print(array.dtype)
# 데이터 타입
print(array[2])
# 세번째 데이터 출력

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 0으로 초기화된 4차원 배열 만들기
array2 = np.zeros((4,4), dtype=float)
print(array2)

array3 = np.ones((3,3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하기 초기화된 3차원 배열 만들기
array4 = np.random.randint(0, 10, (3,3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)

# concatenate 이용하여 두개의 배열 가로축으로 합치기
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1, array2])

print(array3.shape)
print(array3)

# reshape 함수를 이용하여 배열 변경하기
array1 = np.array([1,2,3,4])
array2 = array1.reshape((2,2))

print(array2)

# 두개의 배열 세로로 합치기
array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)

print(array1)
print(array2)

array3 = np.concatenate([array1, array2], axis=0)
print(array3)

# 배열 나누기
array = np.arange(8).reshape(2.4)
left, right = np.split(array, [2], axis=1)
print(left.shape)
print(right.shape)
print(array)
print(left)

Original
https://github.com/ndb796/Python-Data-Analysis-and-Image-Processing-Tutorial