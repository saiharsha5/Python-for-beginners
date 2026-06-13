import numpy as np

a=np.array([1,2,3,4,5])

b=a.reshape(5,1)
print(b)

c=a.shape
print(c)

d=a.dtype
print(d)

e=a.astype(float)
print(e)