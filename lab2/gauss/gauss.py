import numpy

def bubble_max_row(lhs, rhs, k):
    ind = k + numpy.argmax(numpy.abs(lhs[k:, k]))
    if ind != k:
        lhs[[ind, k], :] = lhs[[k,ind], :]
        rhs[[ind, k]] = rhs[[k, ind]]
    return lhs, rhs

def solve_gauss(lhs, rhs):
    if(lhs.shape[0] != lhs.shape[1]):
        raise ValueError("not n*n matrix")
    dimention = lhs.shape[0]
    
    for k in range(dimention - 1):
        lhs, rhs = bubble_max_row(lhs, rhs, k)
        for i in range(k + 1 , dimention):
            coef = lhs[i, k] / lhs[k, k]
            lhs[i, :] -= lhs[k, :] * coef
            rhs[i] -= coef * rhs[k]    

    solution = numpy.zeros(shape=(dimention, 1))
    
    for row in reversed(range(dimention)):
        sum = 0
        for col in reversed(range(row + 1, dimention)):
            sum += lhs[row][col]*solution[col]
        solution[row] = (rhs[row] - sum) / lhs[row][row]
    return solution
