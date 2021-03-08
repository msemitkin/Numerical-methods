import seidel
import numpy

def generate_matrix(dimension):
    lhs = (numpy.random.random((dimension, dimension)) * 100).round()
    rhs = (numpy.random.random((dimension, 1)) * 100).round()

    for row in range(dimension):
        sum = 0
        for col in range(dimension):
            if row != col:
                sum += abs(lhs[row][col])
        if abs(lhs[row][row]) <= sum:
            lhs[row][row] = sum * 1.2
    return lhs, rhs

def hilbert_matrix(dimension):
    matrix = numpy.zeros((dimension, dimension))
    for row in range(dimension):
        for col in range(dimension):
            matrix[row][col] = 1 / (row + col + 1)
    rhs = (numpy.random.random((dimension, 1)) * 100).round()  
    return matrix, rhs         

def check_solution(lhs, rhs, solution):
    dimension = lhs.shape[0]
    lhs_obtained = numpy.zeros_like(rhs)    
    for row in range(dimension):
        sum = 0
        for col in range(dimension):
            sum += lhs[row][col] * solution[col]
        lhs_obtained[row] = sum    
    epsilon = 0.00001
    for row in range(dimension):
        if lhs_obtained[row] - rhs[row] > epsilon:
            return False
    return True   

dimension = 10

lhs, rhs = generate_matrix(dimension)
# lhs, rhs = hilbert_matrix(dimension)

print(lhs)
print(rhs)

solution = seidel.solve_seidel(lhs, rhs)

print(f"solution: {solution.T}")

print(f"Solution is: {check_solution(lhs,rhs, solution)}")