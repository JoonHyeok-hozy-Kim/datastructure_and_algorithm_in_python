### Graph Datastructures are in "DataStructures.graphs"


def DFS(g, u, discovered):
    """ Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    :param g: the target graph to perform DFS
    :param u: the starting vertex
    :param discovered: a dictionary mapping each vertex to the edge that was used to discover it during the DFS
    """
    # print(u)
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


def is_connected(g):
    arbitrary = next(iter(g.vertices()))    # Get an arbitrary vertex from the graph
    d = {}
    DFS(g, arbitrary, d)
    if len(d) != g.vertex_count():
        return False
    elif g._outgoing != g._incoming:
        incoming_d = {}
        _incoming_DFS(g, arbitrary, incoming_d)
        if len(incoming_d) != g.vertex_count():
            return False
    return True


def _incoming_DFS(g, u, discovered, starting=None):
    """ Perform DFS using incoming edges. Going reverse way!
    :param g: the target graph to perform DFS
    :param u: the starting vertex
    :param discovered: a dictionary mapping each vertex to the edge that was used to discover it during the DFS
    """
    if starting is None:
        starting = u
    elif u == starting:     # in order to prevent eternal loop
        return

    # print(u)
    for adjacent in g._incoming:
        for v in g._incoming[adjacent]:
            if v == u:
                discovered[adjacent] = g._incoming[adjacent][u]
                _incoming_DFS(g, adjacent, discovered, starting)


def DFS_complete(g):
    """ Perform DFS for entire graph and return forest as a dictionary.
    :param g: the target graph
    :return: Result maps each vertex v to the edge that was used to discover it. (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None        # u will be the root of the tree
            DFS(g, u, forest)
    return forest
