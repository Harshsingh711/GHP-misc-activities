import numpy as np

A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

product = np.dot(A,B)
print(product)

C = [[2,4],
     [6,8],
     [10,12]]

D = [[5,8,12],
     [12,16,22]]

AB = np.dot(A,B)
BA = np.dot(B,A)
CD = np.dot(C,D)
DC = np.dot(D,C)
AD = np.dot(A,D)
try: 
     BC = np.dot(B,C)
except Exception as e:
     print("All Failed!")
     print(e)