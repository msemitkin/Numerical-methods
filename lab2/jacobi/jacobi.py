import numpy

def solve_jacobi(lhs, rhs):
    if lhs.shape[0] != lhs.shape[1]:
        raise ValueError("not n*n matrix")
    dimension = lhs.shape[0]
    solution = numpy.zeros_like(rhs)
    epsilon = 0.00000001
    while True:
        next_solution = numpy.zeros_like(rhs)
        for row in range(dimension):
            summ = sum([lhs[row][col] * solution[col] for col in range(dimension) if row != col])
            next_solution[row] = (rhs[row] - summ) / lhs[row][row]
        if numpy.allclose(solution, next_solution, atol = epsilon, rtol = 0):
            break
        else:
            solution = next_solution.copy()
    return next_solution    
