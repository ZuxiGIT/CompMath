import math
import numpy as np



def diff_sinus(n, x):
	return math.sin(x + math.pi / 2. * (n % 4))

def get_n_sin(interval, error):
	n = 0

	for x in np.arange(interval[0], interval[1] + error, error):

		while True:
			result = 0

			for i in range(n + 1):
				result += diff_sinus(i, 0.0) * (x**i) / math.factorial(i)

			#print("cuurent n = ", n)
			#print("current x = ", x)
		
			#print(f"f(x) = {math.sin(x)} result = {result}")

			if abs(math.sin(x) - result) < error:
				#print("+++++++++++ found n = ", n)
				break
			else:
				n += 1

	return n 


def diff_exp(n, x):
	return math.exp(x)

def get_n_exp(interval, error):
	n = 0

	for x in np.arange(interval[0], interval[1] + error, error):

		while True:
			result = 0

			for i in range(n + 1):
				result += diff_exp(i, 0.0) * (x**i) / math.factorial(i)

			#print("cuurent n = ", n)
			#print("current x = ", x)
		
			#print(f"f(x) = {math.sin(x)} result = {result}")

			if abs(math.exp(x) - result) < error:
				#print("+++++++++++ found n = ", n)
				break
			else:
				n += 1

	return n 
  
def main():
	print(get_n_sin([0, 1], 1e-3))
	print(get_n_exp([0, 1], 1e-3))
	print(get_n_sin([10, 11], 1e-3))
	print(get_n_exp([10, 11], 1e-3))

if __name__ == "__main__":
	main()
