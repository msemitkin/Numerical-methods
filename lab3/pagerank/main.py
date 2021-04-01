import numpy
import pagerank


def run():
    epsilon = 0.001
    edges = numpy.array([[1, 5], [2, 1], [2, 3], [3, 4], [3, 5], [4, 2], [5, 4], [5, 2]])
    solution = pagerank.find_page_ranks_vector(edges, epsilon)
    print(f"solution: {solution}")


if __name__ == "__main__":
    run()
