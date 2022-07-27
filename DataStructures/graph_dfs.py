

def DFS(g, u, discovered):
    """ Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    :param g: the target graph to perform DFS
    :param u: the starting vertex
    :param discovered: a dictionary mapping each vertex to the edge that was used to discover it during the DFS
    """
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk != u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path