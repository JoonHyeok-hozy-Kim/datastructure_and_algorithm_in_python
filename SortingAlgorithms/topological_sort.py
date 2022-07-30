# For the graph, edge, and vertex datastructures check DataStructures.graphs


def topological_sort(g):
    """
    :param g: an input graph. If graph g has a cycle, the result will be incomplete.
    :return: a list of verticies of directed acyclic graph g in topological order.
    """

    topo = []           # a list of vertices placed in topological order
    ready = []          # list of vertices that have no remaining constraints
    incount = {}        # keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo