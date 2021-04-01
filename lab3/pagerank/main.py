import numpy
import pagerank


def run():
    edges = numpy.array([[1, 5], [2, 1], [2, 3], [3, 4], [3, 5], [4, 2], [5, 4], [5, 2]])
    print(pagerank.get_markov_matrix(edges))


if __name__ == "__main__":
    run()
