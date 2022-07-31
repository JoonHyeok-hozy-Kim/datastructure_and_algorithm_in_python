from DataStructures.priority_queues import AdaptableHeapPriorityQueue



def dijkstra_shortest_path_lengths(g, s):
    """ Compute shortest-path distances from src to reachable vertices of g.
    It uses AdaptableHeapPriorityQueue for the priority queue.
    Suitable for graphs with relatively small number of edges : Recall m < (n^2)/log(n)

    :param g: Graph g can be undirected or directed, but must be weighted such that e.element() returns a numeric weight for each edge e.
    :param s: a distinguished vertex s of G
    :return: dictionary mapping each reachable vertex to its distance from src.
    """

    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pq_locator = {}

    for v in g.vertices():
        if v == s:
        #if v in s:
            d[v] = 0                # d of s, the starting vertex of the path, initialized to 0
        else:
            d[v] = float('inf')     # ds of rest vertices initialized to the positive infinite
        pq_locator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key
        del pq_locator[u]

        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                weight = e.element()
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                pq.update(pq_locator[v], d[v], v)

    return cloud