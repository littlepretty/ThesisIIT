import numpy as np
import glog as log
from pprint import pprint

def printNpMatrix(A, name):
    np.set_printoptions(precision=2, floatmode='fixed')
    print('%s = [' % name)
    for row in A:
        line = ''
        for x in row:
            line += '%.2f, ' % x

        print('\t' + line)
    print(']')


def printNpVector(vector, name):
    np.set_printoptions(precision=2, floatmode='fixed')
    line = '%s = [' % name
    for x in vector:
        line += '%2.2f, ' % x

    print(line + ']')


A = np.array([
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])
D = np.array([
    [3, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
])

invD = np.linalg.inv(D)

Z0 = np.array([[2, 3], [1, 5], [7, 4], [8, 9], [6, 1]])  # X = Z0 = 5 * 2
W0 = np.array([
    [1, 0, 1],
    [0, 1, 0],
])  # 2 * 3
W1 = np.array([
    [0, 1, -2, 2],
    [1, 1, 7, -2],
    [1, 0, -1, 4],
])  # 3 * 4

printNpMatrix(A, 'A')
printNpMatrix(D, 'D')
printNpMatrix(Z0, 'X')

F1 = np.matmul(Z0, W0)
O1 = np.matmul(A, F1)
Z1 = np.matmul(invD, O1)
Z1 = np.maximum(Z1, 0)
printNpMatrix(Z1, "Z1")
# Z1 = np.matmul(np.matmul(np.matmul(invD, A), Z0), W0)

F2 = np.matmul(Z1, W1)
O2 = np.matmul(A, F2)
Z2 = np.matmul(invD, O2)
Z2 = np.maximum(Z2, 0)
printNpMatrix(Z2, "Z2")

Zh = np.concatenate((Z1, Z2), axis=1)
printNpMatrix(Zh, "Zh")
Zsp = np.sort(
    Zh.view('f8,f8,f8,f8,f8,f8,f8'),
    order=['f6', 'f5', 'f4', 'f3', 'f2', 'f1', 'f0'],
    axis=0)[::-1]
Zsp = np.concatenate((Zsp['f0'], Zsp['f1'], Zsp['f2'], Zsp['f3'], Zsp['f4'],
                      Zsp['f5'], Zsp['f6']),
                     axis=1)
printNpMatrix(Zsp, "Zsp")

# Weight vertices
W = np.array([.4, .1, .5])
E = np.matmul(W, Zsp[0:3, :])
printNpVector(E, 'E')
