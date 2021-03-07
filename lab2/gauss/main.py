import gauss
import numpy
def check_solution(lhs, rhs, solution):
    dimention = lhs.shape[0]
    for row in range(dimention):
        sum = 0
        for col in range(dimention):
            sum += lhs[row][col] * solution[0][col]
        epsilon = 0.00000001
        if sum - rhs[row] > epsilon:
            return False
    return True                        


def generate_system(dimention):
    lhs = (numpy.random.rand(dimention, dimention) * 10).round()
    rhs = (numpy.random.rand(dimention, 1) * 10).round()
    return lhs, rhs

dimention = 10

lhs, rhs = generate_system(dimention)

print(f"lhs: {lhs}")
print(f"rhs: {rhs}")

solution = gauss.solve_gauss(lhs, rhs).T

print(f"Solution: {solution}")
print(f"Solution is: {check_solution(lhs, rhs, solution)}")