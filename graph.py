# Tuple representation of an edge in the format (weight, a, b)
Edge = tuple[int, int, int]


class Graph:
    """Graph data structure implemented using an adjacency matrix"""

    def __init__(self, node_count: int):
        if node_count < 0:
            raise ValueError("Node count must be non-negative")

        self.count = node_count
        self.__matrix: list[list[None | int]] = [
            [None for _ in range(node_count)] for _ in range(node_count)
        ]

    def add_edge(self, a: int, b: int, weight: int):
        """Creates an edge from node `a` to `b` of magnitude `weight`"""
        if not (0 <= a < self.count and 0 <= b < self.count):
            raise ValueError(f"Nodes must be in range {0}-{self.count - 1}")

        self.__matrix[a][b] = weight
        self.__matrix[b][a] = weight

    def get_edge(self, a: int, b: int) -> int | None:
        """Returns the weight of the edge connecting `a` and `b`, and `None` if no edge exists"""
        if not (0 <= a < self.count and 0 <= b < self.count):
            raise ValueError(f"Nodes must be in range {0}-{self.count - 1}")

        return self.__matrix[a][b]

    def is_connected(self, a: int) -> bool:
        """Returns `True` if `a` is connected to the graph"""
        return any(w is not None for w in self.__matrix[a])

    def neighbours(self, a: int) -> list[Edge]:
        """Returns all neighbours of `a` and the edges"""
        return [(w, a, b) for b, w in enumerate(self.__matrix[a]) if w is not None]

    def edges(self) -> list[Edge]:
        """Returns all edges in the graph"""
        edges: list[Edge] = []
        for i in range(self.count):
            for j in range(i, self.count):
                weight = self.__matrix[i][j]
                if weight is not None:
                    edges.append((weight, i, j))
        return edges

    def __repr__(self) -> str:
        s = ""
        for i in range(self.count):
            for j in range(i, self.count):
                if self.__matrix[i][j] is not None:
                    s += f"{chr(i + 65)} <-{self.__matrix[i][j]}-> {chr(j + 65)}\n"
        return s
