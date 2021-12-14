import random as rnd
import numpy  as np
import math


def f1(vec):
    return math.tan(vec[1] - vec[0]) + vec[0] * vec[1] - 0.3

def f2(vec):
    return vec[0] ** 2 + vec[1] ** 2 - 1.5


def diff_x(f, vec, prec):
    return (f([vec[0] + prec, vec[1]]) - f(vec)) / prec


def diff_y(f, vec, prec):
    return (f([vec[0], vec[1] + prec]) - f(vec)) / prec

def ro(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def Newton(func_vec, prec):
    rnd.seed()

    point_prec = prec * math.sqrt(2)

    u_k = [rnd.uniform(-10, 10), rnd.uniform(-10, 10)]

    f1 = func_vec[0]
    f2 = func_vec[1]
    F = lambda x: [func_vec[0](x), func_vec[1](x)]

    u_k_1= [0, 0]

    while True:
        J_inv = np.linalg.inv(np.asarray([[diff_x(f1, u_k, prec), diff_y(f1, u_k, prec)],
                                         [diff_x(f2, u_k, prec), diff_y(f2, u_k, prec)]]))

        u_k_1 = u_k - np.dot(J_inv, F(u_k))

        if ro(u_k_1, u_k) < point_prec:
            break

        u_k = u_k_1 

    return u_k_1

def main():
    print(Newton([f1, f2], 1e-6))

if __name__ == "__main__":
    main()
