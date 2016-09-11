# Matrix Algebra

# Insert the given vectors/ matrices

import numpy
from numpy import linalg as LA

A = numpy.matrix([[1, 2, 3], [2, 7, 4]])
B = numpy.matrix([[1, -1], [0,2]])
C = numpy.matrix([[5, -1], [9,1], [6,0]])
D = numpy.matrix([[3, -2, -1], [1, 2, 3]])
u = numpy.array([6, 2, -3, 5])
v = numpy.array([3, 5, -1, 4])
w = numpy.array([[1], [8], [0], [5]])


# Exercise 1

dimA = A.shape
dimB = B.shape
dimC = C.shape
dimD = D.shape
dimu = u.shape
dimw = w.shape


print "Answer 1.1): ", dimA
print "Answer 1.2): ", dimB
print "Answer 1.3): ", dimC
print "Answer 1.4): ", dimD
print "Answer 1.5): ", dimu
print "Answer 1.6): ", dimw

#Exercise 2

alpha = 6


print "Answer 2.1: ", u+v
print "Answer 2.2: ", u-v
print "Answer 2.3: ", alpha * u
print "Answer 2.4: ", numpy.dot(u, v)
print "Answer 2.5: ", LA.norm(u)

#Exercise 3

print "Answer 3.1: not defined."
print "Answer 3.2: ", A - C.transpose()
print "Answer 3.3: ", C.transpose() + 3*D
print "Answer 3.4: ", numpy.dot(B, A)
print "Answer 3.5: not defined"

