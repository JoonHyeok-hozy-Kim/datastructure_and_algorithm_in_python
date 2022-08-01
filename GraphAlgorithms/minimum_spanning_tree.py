

from DataStructures.priority_queues import AdaptableHeapPriorityQueue
def MST_PrimJarnik(g):
    """ Compute a minimum spanning tree of weighted graph g.

    :param g: a weighted graph
    :return: Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}
    tree = []
    pq = AdaptableHeapPriorityQueue()
    pq_locator = {}

    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0            # Initialization with an arbitrary initial vertex
        else:
            d[v] = float('inf')
        pq_locator[v] = pq.add(d[v],            # distance as the key
                               (v, None))       # vertex and the edge(initialized to None at first) as the value

    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value
        del pq_locator[u]

        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pq_locator:
                weight = link.element()
                if weight < d[v]:
                    d[v] = weight
                    pq.update(pq_locator[v], d[v], (v, link))
    return tree