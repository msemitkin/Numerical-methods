import numpy
import collections


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
            print(markov_matrix)
    return markov_matrix


def count_references(graph_edges):
    return collections.Counter(graph_edges[:, 0])


def exists_edge_between(edges, from_vertex, to_vertex):
    print(len(edges))
    for index in range(len(edges)):
        if numpy.array_equal(numpy.array([from_vertex, to_vertex]), edges[index, :]):
            return True
    return False


def count_vertices(graph_edges):
    return max(graph_edges[:, 0])


if __name__ == "__main__":
    pass
