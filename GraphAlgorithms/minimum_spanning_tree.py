from DataStructures.priority_queues import HeapPriorityQueue, AdaptableHeapPriorityQueue


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
            # print('Initial vertex : {}'.format(v))
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


from DataStructures.partition import TreePartition as Partition
def MST_Kruskal(g):
    """ Compute a minimum spanning tree of a graph using Kruskal s algorithm.

    :param g: The elements of the graph s edges are assumed to be weights.
    :return: a list of edges that comprise the MST.
    """
    tree = []
    pq = HeapPriorityQueue()
    forest = Partition()        # Check disjoint partitions!
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)

    size = g.vertex_count()
    while len(tree) != size-1 and not pq.is_empty():
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
    return tree