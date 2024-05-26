from typing import TypedDict


class Node(TypedDict):
    """Helper class to represent a node in DisjointSets"""

    next: int | None
    value: int
    parent: int


class DisjointSets:
    """A collection of sets"""

    def __init__(self):
        self.nodes: list[Node] = []

    def make_set(self, a: int):
        """Creates a set with a single element `a`"""
        self.nodes.append(
            {
                "next": None,
                "parent": a,
                "value": a,
            }
        )

    def find_set(self, a: int) -> int | None:
        """Finds the representative of the set which contains `a`"""
        for node in self.nodes:
            if node["value"] == a:
                return node["parent"]

    def union(self, a: int, b: int):
        """Joints the two sets containing `a` and `b`"""
        parent_a = self.find_set(a)
        parent_b = self.find_set(b)

        if parent_a is None or parent_b is None:
            return

        for node in self.nodes:
            if node["parent"] == parent_a:
                node["parent"] = parent_b
