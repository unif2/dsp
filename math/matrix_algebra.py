Q1

# Matrix Algebra

import numpy as np
import math

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = (np.array([[1,8,0,5]])).transpose()

matrix_list = [A,B,C,D,u,w]

for m in matrix_list:
	print('The dimensions are: \n',m.shape)

Q2

alpha = 6
print(u + v)
print(u - v)
print(alpha*u)
print(u.dot(v.transpose()))
print(math.sqrt(u.dot(u.transpose())))

Q3

print(A+C) # Not defined
print(A - C.transpose())
print(C.transpose() + 3*D)
print(B.dot(A))
print(B.dot(A.transpose())) # Not defined
print(B.dot(C)) # Not defined
print(C.dot(B))
print((B.dot(B)).dot(B.dot(B)))
print(A.dot(A.transpose()))
print((D.transpose()).dot(D))
