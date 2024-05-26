from random import randint

from graph import Edge, Graph
from disjoint_sets import DisjointSets


def prims(graph: Graph) -> Graph:
    if not all(graph.is_connected(i) for i in range(graph.count - 1)):
        raise ValueError("The graph must be fully connected to run Prim's algorithm")

    T = Graph(graph.count)
    # Could use a heap to speed up removal of min
    fringe_edges: set[Edge] = set()

    # Initialise T with fringe edges from a random node
    first = randint(0, graph.count - 1)
    for weight, _, neighbour in graph.neighbours(first):
        fringe_edges.add((weight, first, neighbour))

    while fringe_edges:
        next = min(fringe_edges)
        fringe_edges.remove(next)
        weight, node, other = next

        if not T.is_connected(other):
            T.add_edge(node, other, weight)

        for weight, _, neighbour in graph.neighbours(other):
            if not T.is_connected(neighbour):
                fringe_edges.add((weight, other, neighbour))

    return T


def kruskal(graph: Graph):
    F = Graph(graph.count)
    S = DisjointSets()

    edges = sorted(graph.edges())

    for i in range(graph.count):
        S.make_set(i)

    for weight, u, v in edges:
        if S.find_set(u) != S.find_set(v):
            F.add_edge(u, v, weight)
            S.union(u, v)

    return F
