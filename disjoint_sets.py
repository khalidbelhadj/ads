class Node:
    """Helper class to represent a node in DisjointSets"""

    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None
        self.parent: Node | None = None


class DisjointSets:
    """A collection of sets"""

    def __init__(self):
        self.nodes: list[Node] = []

    def get_node(self, a: int) -> Node:
        return next(x for x in self.nodes if x.value == a)

    def make_set(self, a: int):
        """Creates a set with a single element `a`"""
        node = Node(a)
        node.parent = node
        self.nodes.append(node)

    def find_set(self, a: Node) -> Node | None:
        """Finds the representative of the set which contains `a`"""
        return a.parent

    def union(self, a: Node, b: Node):
        """Joints the two sets containing `a` and `b`"""
        parent_a = self.find_set(a)
        parent_b = self.find_set(b)

        if parent_a is None or parent_b is None:
            return

        current = parent_a
        while current.next is not None:
            current.parent = parent_b
            current = current.next
        current.parent = parent_b
        current.next = b
