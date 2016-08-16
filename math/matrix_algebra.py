Q1

# Matrix Algebra

import numpy as np

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


