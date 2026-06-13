import numpy as np

zero=np.array(10)
print(zero)
print(type(zero))
print("Dimension : ",zero.ndim)
print("Bytes : " ,zero.nbytes)


one=np.array([12,24,36,48,60])
print(one)
print(type(one))
print("Dimension : ",one.ndim)
print("Bytes : ",one.nbytes)

two=np.array([[12,24,48],[65,33,44]])
print(two)
print(type(two))
print("Dimension : ",two.ndim)
print("Bytes : ",two.nbytes)

three=np.array([[[12,24,36,60],[24,56,78,54]],[[23,21,11,22],[24,77,65,85]]])
print(three)
print(type(three))
print("Dimension : ",three.ndim)
print("Bytes : ",three.nbytes)