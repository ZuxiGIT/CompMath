x_array = [0,   1,   2,   5,   7]
f_array = [1, 0.5, 0.3, 0.2, 0.1]

def Newton_inter(x_list):
	length = len(x_list)
	if length == 1:
		return f_array[x_array.index(x_list[0])]
	else:
		return (Newton_inter(x_list[1:]) - Newton_inter(x_list[:-1])) / (x_list[-1] - x_list[0])

def get_func_value(x):
	result = 0
	args = []
	for i in range(len(x_array)):
		args.append(x_array[i]) 

		temp = Newton_inter(args)

		for j in range(i):
			temp *= (x - x_array[j]) 

		result += temp 

	return result

def diff(f, x):
	return (f(x + 1e-3) - f(x)) / 1e-3 

print(diff(get_func_value, 2))
