import numpy
import collections


def find_page_ranks_vector(graph_edges, epsilon):
    lmbd = 0.85
    markov_matrix = get_markov_matrix(graph_edges)
    modified_markov_matrix = get_modified_markov_matrix(lmbd, markov_matrix)
    dimension = len(markov_matrix)
    initial_solution = numpy.full(dimension, 1 / dimension)
    while True:
        next_solution = numpy.matmul(modified_markov_matrix, initial_solution)
        if numpy.allclose(next_solution, initial_solution, epsilon, 0):
            return next_solution
        initial_solution = next_solution


def get_modified_markov_matrix(lmbd, markov_matrix):
    dimension = len(markov_matrix)
    return lmbd * markov_matrix + (1 - lmbd) * numpy.full((dimension, dimension), 1 / dimension)


def get_markov_matrix(graph_edges):
    vertices_number = count_vertices(graph_edges)
    references_counts = count_references(graph_edges)
    markov_matrix = numpy.zeros((vertices_number, vertices_number))
    for i in range(vertices_number):
        to_vertex = i + 1
        for j in range(vertices_number):
            from_vertex = j + 1
            if exists_edge_between(graph_edges, from_vertex, to_vertex):
                markov_matrix[i][j] = 1 / references_counts.get(from_vertex)
    return markov_matrix


def count_references(graph_edges):
    return collections.Counter(graph_edges[:, 0])


def exists_edge_between(edges, from_vertex, to_vertex):
    for index in range(len(edges)):
        if numpy.array_equal(numpy.array([from_vertex, to_vertex]), edges[index, :]):
            return True
    return False


def count_vertices(graph_edges):
    return max(graph_edges[:, 0])


if __name__ == "__main__":
    pass
