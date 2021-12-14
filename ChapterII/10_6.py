import numpy as np
import math

def FillMatrix(a, b, c, p, n):

    matrix = np.zeros((n + 1, n + 1))

    for row in range(0, n):

        column = row

        if(row == 0):
            matrix[row][column] = b[column]
            matrix[row][column + 1] = c[column]
        else:
            matrix[row][column - 1] = a[column]
            matrix[row][column]     = b[column]
            matrix[row][column + 1] = c[column]

    for i in range(0, n+1):
        matrix[n][i] = p[i]

    #matrix[3][1] = 10000

    #print(matrix)
    #print(np.shape(matrix))

    return matrix

   

def vec_norm(vec):
    return math.sqrt( sum( [vec[i] * vec[i] for i in range(len(vec))]))

def Seidel(A, f, error):

    x_k_1 = [0 for i in range(len(A))]
    x_k = [0 for i in range(len(A))]

    
    #print(len(A))
    while(np.linalg.norm(A @ x_k_1 - f) > error): 

        x_k = x_k_1.copy()

        for i in range(0, len(A)):
            x_k_1[i] = f[i]

            for j in range(0, i):
                x_k_1[i] = x_k_1[i] - A[i][j] * x_k_1[j]

            for j in range(i+1, len(A)):
                x_k_1[i] = x_k_1[i] - A[i][j] * x_k[j]

            x_k_1[i] = x_k_1[i] / A[i][i]

        #print(A)
        #print(A@x_k_1)
        #print(np.dot(A, x_k_1))
        #print(f"x_k = {x_k}\nx_k_1 = {x_k_1}")
        #print("----> ", np.linalg.norm(A@x_k_1 - f)) 

    return x_k_1

def Gauss(A, f, error):

    #print(A)
    def DivideRow(A, f, num, val):
        A[num] /= val 
        f[num] /= val 

    def SubRows(A, f, src, dst, val):
        A[dst] = A[dst] - val * A[src]
        f[dst] = f[dst] - val * f[src]

    for row in range(len(A)):
        DivideRow(A, f, row, A[row][row])
        for i in range(len(A)):
            if(i == row):
                continue
            SubRows(A, f, row, i, A[i][row])
        #print(A)
    
    #print(A)
    return f

def mat_norm(A):
    max_ = -1
    for i in range(len(A)):
        temp = 0
        for j in range(len(A)):
            temp += abs(A[i][j])
        if(temp > max_): max_ = temp
    return max_

def CondNumber(A):
    return mat_norm(A) * mat_norm(np.linalg.inv(A)) 

def main():
    n = 19

    a = [0]
    a.extend([1  for i in range(1, n)])

    b = [1]
    b.extend([-2 for i in range(1,n)])

    c = [0]
    c.extend([1  for i in range(1, n)])

    f = [1]
    f.extend([2 / (i*i) for i in range(1, n)])
    f.append(-n / 3)

    p = [1]
    p.extend([2 for i in range(1, n)])
    p.append(1)
    #print(f)
    #print(f"shape = {np.shape(a)}")

    matrix = FillMatrix(a, b, c, p, n)
    #print(matrix)
    #A = np.random.rand(n,n) + n * np.eye(n)
    #B = np.random.rand(n)   
    #matrix = np.asarray([[100, 30, -70], [15, -50, -5], [6, 2, 20]]) 
    #f = [60, -40, 28]
    print(f"----> Seidel says x =\n {Seidel(matrix.copy(), f.copy(), 1e-3)}")
    print(f"----> numpy  says x =\n {list(np.linalg.solve(matrix.copy(), f.copy()))}")
    #A = np.array([[1.,3.,0.,0.], [6.,3.,1,0. ], [0.,6.,2.,4.], [0.,0.,2.,1.]])
    #B = np.array([5.,6.,5.,9.])
    #print(f"----> Gauss  says x =\n {Gauss(A, B, 1e-3)}")
    print(f"----> Gauss  says x =\n {Gauss(matrix.copy(), f.copy(), 1e-3)}")
    print(f"---->Condnumber = {CondNumber(matrix)}")
    lambdas = np.linalg.eigvals(matrix.copy())
    print(f"---->lambda_max = {max(lambdas)} lambda_min = {min(lambdas)}")


if __name__ == "__main__":
    main()

