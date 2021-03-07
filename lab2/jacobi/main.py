import numpy
import jacobi

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

def check_solution(lhs, rhs, solution):
    dimension = lhs.shape[0]
    for row in range(dimension):
        sum = 0
        for col in range(dimension):
            sum += lhs[row][col] * solution[col]
        epsilon = 0.00001
        if sum - rhs[row] > epsilon:
            print(sum)
            print(rhs[row])
            return False
    return True   

dimension = 10

lhs, rhs = generate_matrix(dimension)

print(lhs)
print(rhs)

solution = jacobi.solve_jacobi(lhs, rhs)

print(f"solution: {solution.T}")

print(f"Solution is: {check_solution(lhs,rhs, solution)}")