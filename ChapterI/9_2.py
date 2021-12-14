import matplotlib.pyplot as plot  
import numpy as np


def Horner(coeff, x__arr):
    result = coeff[0]
    for i in range(1, len(coeff)): result = result * x__arr + coeff[i]
    return result

def main():
    #Input Data
    polynom  = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]
    interval = [1.92, 2.08]
    #interval = [-3, 3]
    step     = 10 ** (-4)
    
    x_array  = np.arange(interval[0], interval[1] + step, step)
    
    #Values
    horner_value = Horner(polynom, x_array)
    poly_value   = (x_array - 2)**9

    #Graphs appearance
    plot.figure(figsize = (38, 10))
    plot.title('Horner approximation')
    plot.rc('font', **{'size' : 22})
    plot.grid()

    #Graph data
    plot.plot(x_array, horner_value, color = 'red')
    plot.plot(x_array, poly_value, color = 'green', linewidth = 3)
    plot.show()
        
if __name__ == "__main__":
    main()
