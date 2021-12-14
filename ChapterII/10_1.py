import random
import math
import numpy


def main():
    random.seed()

    A = numpy.asarray([[0, -7, 7], [-7, -9, -5], [7, -5, -1]])
    u_k = [random.uniform(-10, 10) for i in range(3)]

    error = 1e-10
    eig = 0
    eig_1 = 10 

    while abs(eig_1- eig) > error:
        eig = eig_1 
        u_k_1 = numpy.dot(A, u_k)

        eig_1 = numpy.dot(u_k_1, u_k) / numpy.dot(u_k, u_k)

        u_k = u_k_1

    print(eig)
if __name__ == "__main__":
    main()
