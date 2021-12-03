import math 
import numpy as np

step = 1e-6 

def Trap_integr(f, _range):
	result = 0

	for i in np.arange(_range[0], _range[1], step):
		result += step * (f(i) + f(i + step)) / 2

	return result

def function(x):
	return math.cos(100 * x) * math.log(x)

print(Trap_integr(function, (1, 2)))
