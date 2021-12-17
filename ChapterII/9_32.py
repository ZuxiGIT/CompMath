import numpy as np
import math

def vec_norm(vec):
    return math.sqrt( sum( [vec[i]*vec[i] for i in range(len(vec)) ]) )

def mat_norm(A):
    max_ = -1
    for i in range(len(A)):
        temp = 0
        for j in range(len(A)):
            temp += abs(A[i][j])
        if(temp > max_): max_ = temp
    return max_

def main():
    A = np.asarray([[ 4,  2, -1, 2],
                    [ 2,  4,  1, 3],
                    [-1,  1,  3, 2],
                    [ 2,  3,  2, 5]])
    
    min_eig = min(abs(np.linalg.eig(A)[0]))
    max_eig = max(abs(np.linalg.eig(A)[0]))

    optimal_tau = 2 / (min_eig + max_eig)
    print(optimal_tau)
    #B =
    #min_eig = min(abs(np.linalg.eig(A)[0]))
    #max_eig = max(abs(np.linalg.eig(A)[0]))

    #optimal_tau_arbitary = 2 / 
    print(A)
    print(A*A)

    tau_1_opt = -1
    tau_2_opt = -1 
    R_norm = 1

    print(10*np.eye(len(A)))
    coeff = 1e3
    for tau_1 in np.arange(0, 1, 1/coeff):
        for tau_2 in np.arange(0, 1, 1/coeff ):
            tau_1 /= coeff
            tau_2 /= coeff
            E = np.eye(len(A))
            Mat_norm = mat_norm((E - tau_1 * A) - tau_2*A @ (E - tau_1*A))
            print(Mat_norm)
            if(tau_1 == 0 or tau_2 == 0):
                continue
            if(Mat_norm < R_norm):
               print(f"t_1 = {tau_1} t2 = {tau_2}")
               tau_1_opt = tau_1
               tau_2_opt = tau_2
               R_norm = Mat_norm

    print(tau_1_opt)
    print(tau_2_opt)
    print(R_norm)
            


if __name__ == "__main__":
    main()
