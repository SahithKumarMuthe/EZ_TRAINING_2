'''a=[[1,2],
[3,4]]
b=[[0,0],
[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for r in b:
    a=str(r[::-1])
    print(a)'''
a=[[1,2],
[3,4]]
b=[[0,0],
[0,0]]
import numpy as np
c=np.transpose(a)
d=c[::-1]
print(d)
  
