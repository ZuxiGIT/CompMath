x_array = [-0.9, -0.6, 0.3, 0.6]
f_array = [ 0.1,  0.2, 0.3, 0.4]

def Newton_inter(x_list):
	length = len(x_list)
	if length == 1:
		return f_array[x_array.index(x_list[0])]
	else:
		return (Newton_inter(x_list[1:]) - Newton_inter(x_list[:-1])) / (x_list[-1] - x_list[0])

def get_value_func(x):
	result = 0
	args = []
	for i in range(len(x_array)):
		args.append(x_array[i])
		temp = Newton_inter(args)
		for j in range(i):
			temp*= (x - x_array[j]) 

		result += temp

	return result


def diff(f, x):
    return (f(x + 1e-3) - f(x)) / 1e-3

#f^(4) = (f(x+4h) - 4f(x+3h) + 6f(x+2h) - 4f(x+h) + f(x)) / h^4

def error(func):
    h = 1e-4
    res = 1;
    for i in x_array[:-1]:
        res *= i 
    return (-1)**len(x_array[:-1]) * res * (func(4*h) - 4*func(3*h) + 6*func(2*h) - 4*func(h) + func(0)) / (h**4) / 24

print("error = ", error(get_value_func))
print(get_value_func(0))
