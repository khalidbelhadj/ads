from random import randint

from graph import Edge, Graph
from disjoint_sets import DisjointSets


def prims(graph: Graph) -> Graph:
    """Computes the minimum spanning tree using Prim's algorithm"""
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


def kruskal(graph: Graph) -> Graph:
    """Computes the minimum spanning tree using Krukal's algorithm and the disjoint set data structure"""
    F = Graph(graph.count)
    S = DisjointSets()

    edges = sorted(graph.edges())

    for i in range(graph.count):
        S.make_set(i)

    edges = [(w, S.get_node(a), S.get_node(b)) for (w, a, b) in edges]

    for weight, u, v in edges:
        if S.find_set(u) != S.find_set(v):
            F.add_edge(u.value, v.value, weight)
            S.union(u, v)

    return F

def mst_example():
    g = Graph(5)

    g.add_edge(0, 2, 3)
    g.add_edge(2, 1, 10)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(1, 3, 4)
    g.add_edge(3, 4, 1)

    print(prims(g))
    print(kruskal(g))