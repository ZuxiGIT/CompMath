import numpy as np
import matplotlib.pyplot as plot

H = [8,  10, 15,   20,   30,   40,   60,   80]
B = [13, 14, 15.4, 16.3, 17.2, 17.8, 18.5, 18.8]

def func(a, b, x): return x / (a + b * x)

def main():
    A = np.asarray( [[B[i], B[i]*H[i]]  for i in range(len(B))])
    #print(matrix)
    xsi = np.asarray(H)
    res = np.transpose(A) @ xsi @ np.linalg.inv( np.transpose(A) @ A)
    print(res)

    a = res[0]
    b = res[1]
    interval  = (8, 80)
    step      = 0.1
    x_array   = np.arange(interval[0], interval[1] + step, step)
    appr_func = func(a, b, x_array)

    #Graph appearance
    plot.figure(figsize = (38, 10))
    plot.title('Magnetic field approximation')
    plot.rc('font', **{'size' : 22})
    plot.grid()

    #Graph data
    for i in range(0, len(H)): plot.scatter(H[i], B[i], color = 'red', marker = 'o', linewidth = 4)
    plot.plot(x_array, appr_func, color = 'blue', linewidth = 3)
    plot.show()

if __name__ == "__main__":
    main()
