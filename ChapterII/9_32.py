import numpy as np

def main():
    A = np.asarray([[4, 2, -1, 2], [2, 4, 1, 3], [-1, 1, 3, 2], [2, 3, 2, 5]])
    
    min_eig = min(abs(np.linalg.eig(A)[0]))
    max_eig = max(abs(np.linalg.eig(A)[0]))

    optiomal_tau = 2 / (min_eig + max_eig)
    B = 
    min_eig = min(abs(np.linalg.eig(A)[0]))
    max_eig = max(abs(np.linalg.eig(A)[0]))

    optimal_tau_arbitary = 2 / 
    print(A)
    print(A*A)

if __name__ == "__main__":
    main()
