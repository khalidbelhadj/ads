import heapq


Graph = dict[str, list[tuple[int, str]]]


g: Graph = {
    "a": [(1, "b"), (2, "c")],
    "b": [(1, "a"), (3, "c"), (4, "d")],
    "c": [(2, "a"), (3, "b"), (5, "d")],
    "d": [(4, "b"), (5, "c")],
    "e": [(6, "f")],
    "f": [(6, "e")],
}


def prims_mst(graph: Graph) -> Graph:
    first_node = list(graph.keys())[0]

    mst: Graph = {first_node: []}

    fringe_nodes = [
        (
            weight,
            id,
            first_node,
        )
        for (weight, id) in graph[first_node]
    ]
    heapq.heapify(fringe_nodes)

    while fringe_nodes:
        weight, id, parent = heapq.heappop(fringe_nodes)

        mst[parent].append((weight, id))
        if id not in mst.keys():
            pass

        for fringe_weight, fringe_id in graph[id]:
            if fringe_id not in mst.keys():
                heapq.heappush(fringe_nodes, (fringe_weight, fringe_id, id))

    print(mst)

    return mst


def kruskals_mst(graph: Graph):
    raise NotImplementedError


prims_mst(g)
