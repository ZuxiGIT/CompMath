import math

def main():
#Input data
    Euler = 0.57721566490153286061 
    result = 0                      
    summ = 0                       
    iteration = 1                      
    error     = 1e-10 

    temp = result + 10 
    while (abs(temp - result) >= error):
        summ += 1 / iteration 

        temp = result

        result = summ - math.log1p(iteration)
        
        iteration += 1


    print('Число итераций, при котором получилась приближенная константа:', iteration)
    print('Реальная константа: ', Euler, '\nКонстанта программы: ', result)

if __name__ == "__main__":
    main()
