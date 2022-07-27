

def BFS(g, s, discovered):
    """ Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    :param g: the target graph
    :param s: a vertex
    :param discovered: a dictionary mapping each vertex to the edge that was used to
    :return:
    """
    level = [s]                 # first level includes only s
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level
