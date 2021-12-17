import numpy as np

#year
x = [1910 + i*10 for i in range(10)]
#population
y = [92228496, 106021537, 123202624, 132164569,
     151325798, 179323175, 203211926, 226545805,
     248709873, 281421906 ]

def dot(f1, f2):
    res = 0
    for i in range(len(x)):
        res += f1(x[i])*f2(x[i])

    return res

def func(n):
    return lambda x: (x - 1955) ** n

def coeff_matrix(N):
    #matrix_ = np.asarray([[ [i, j]  for j in range(N + 1) ] for i in range(N + 1) ] )
    #print(matrix_)
    matrix = [[dot(func(i), func(j)) for j in range(N + 1) ] for i in range(N + 1) ]
    print("mat\n", matrix)
    #print(np.transpose(matrix))
    return matrix 

def vec_f(N):
    y_func = lambda x_: y[x.index(x_)]

    #print(y_func(1910))
    vec =  [dot(func(i), y_func)  for i in range(N+1) ]
    print("vec ", vec)
    return vec 

def matrix_minor(matrix, i, j): 
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):

    if len(matrix) == 2: return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant_ = 0

    determinant_ = sum( (-1)**col * matrix[0][col] * determinant(matrix_minor(matrix, 0, col)) for col in range(len(matrix)))

    return determinant_



def cramer(matrix, vec):
    det_mat = determinant(matrix)
    
    res = []
    for i in range(len(matrix)):
        temp = matrix.copy() 
        for j in range(len(matrix)):
            temp[j][i] = vec[j] 
        res.append(determinant(temp) / det_mat)

    print("sol ", res)
    return res 

def poly(coeff, x, N):
    res = sum( coeff[i] * func(i)(x) for i in range(N))
    return res

def main():
    N = 2
    print(dot(func(0), func(2)))
    #print(dot(func(2), func(0)))

    print(poly(cramer(coeff_matrix(N), vec_f(N)), 2010, N))

if __name__ == "__main__":
    main()
