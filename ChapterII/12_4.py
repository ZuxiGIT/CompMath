import random as rnd
import numpy  as np
import math

def diff(f, x, prec):
	return (f(x + prec) - f(x)) / prec


def f1(x):
	return (0.5 ** x) - ((x - 1) ** 2) + 1

#roots
	#-5.25
	#-0.57
	#2.109


def f2(x):
	return x ** 2 - math.exp(x) / 5

#roots
	#-0.37
	#0.60
	#4.70


def Newton(f, prec):
    rnd.seed()

    x = rnd.uniform(-10, 10)

    x_next = 0

    n = 0

    while True:
        x_next = x - f(x) / diff(f, x, prec)

        if abs(x - x_next) < prec:
            break

        x = x_next


    return x_next 

def secants_with_loc(f, prec):
    rnd.seed()

    a = rnd.uniform(-10, 0) 

    b = rnd.uniform(0, 10)
    while(f(a) * f(b) > 0):
        b = rnd.uniform(0, 10)
    

    while True:

        c = (a * f(b) - b * f(a)) / (f(b) - f(a)) 

        if abs(f(a)) < prec or abs(f(b)) < prec:
            break

        if(f(b) * f(c) < 0):
            a = c
        elif(f(a) * f(c) < 0):
            b = c

        print(f"[{a}, {b}]")
    return c

def secants(f, prec):

    x_k = rnd.uniform(-10, 10) 
    x_k_1 = rnd.uniform(-10, 10)

    while True:
        temp = x_k_1
        x_k_1 = (x_k_1 * f(x_k) - x_k * f(x_k_1)) / (f(x_k) - f(x_k_1)) 
        x_k = temp

        if abs(f(x_k)) < prec or abs(f(x_k_1)) < prec:
            break

    return x_k_1 


def main():
    print(Newton(f1, 1e-3))
    print(secants_with_loc(f1, 1e-3))
    print(secants(f1, 1e-3))

if __name__ == "__main__":
	main()
