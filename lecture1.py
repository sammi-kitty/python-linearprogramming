from scipy.optimize import linprog
import numpy as np

def main():
    solution8_22 = problem8_22()
    print(solution8_22.fun)
    
def problem8_22():
    # Network, find longest path
    A_ub = np.array([
        [-1,  1,  0,  0,  0,  0],
        [-1,  0,  1,  0,  0,  0],
        [ 0, -1,  1,  0,  0,  0],
        [ 0,  0, -1,  0,  1,  0],
        [ 0, -1,  0,  1,  0,  0],
        [ 0,  0,  0,  0, -1,  1],
        [ 0,  0,  0, -1,  1,  0]
    ]) * (-1)
    b_ub = np.array([[
        6,
        5,
        0,
        4,
        3,
        3,
        0
    ]]) * (-1)
    A_eq = np.array([[
        1, 0, 0, 0, 0, 0
    ]])
    b_eq = np.array([0])

    c = np.array([
        -1, 0, 0, 0, 0, 1
    ])

    program = linprog(
        c = c, A_ub = A_ub, b_ub = b_ub, A_eq = A_eq, b_eq = b_eq, bounds = [None, None]
    )
    return program

main()
