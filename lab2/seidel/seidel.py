import numpy

def solve_seidel(lhs, rhs):
    if lhs.shape[0] != lhs.shape[1]:
        raise ValueError("not n*n matrix")
    dimension = lhs.shape[0]
    solution = numpy.zeros_like(rhs)
    
    while True:
        next_solution = numpy.zeros_like(rhs)
        for row in range(dimension):
            sum = 0
            for col in range(row):
                sum += lhs[row][col] * next_solution[col]                
            for col in range(row + 1, dimension):
                sum += lhs[row][col] * solution[col]
            next_solution[row] = (rhs[row] - sum) / lhs[row][row]
        if numpy.allclose(solution, next_solution, atol = 0.000000001, rtol = 0):
            break
        solution = next_solution

    return next_solution