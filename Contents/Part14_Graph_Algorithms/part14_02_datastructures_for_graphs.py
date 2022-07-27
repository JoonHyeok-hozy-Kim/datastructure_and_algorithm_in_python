



if __name__ == '__main__':

    pass

    from DataStructures.graphs import Graph, DFS

    g = Graph()
    even = None
    odd = None
    for i in range(10):
        if i%2 == 0:
            even = g.insert_vertex(i)
            if odd is not None:
                g.insert_edge(odd, even)
        else:
            odd = g.insert_vertex(i)
            new_edge = g.insert_edge(even, odd)

    # for v in g.vertices():
    #     print(v.element())
    #
    # for e in g.edges():
    #     print('{} - {}'.format(e._origin.element(), e._destination.element()))
    #
    # for v in g.vertices():
    #     print('Vertex : {}'.format(v.element()))
    #     for i in g.incident_edges(v):
    #         print('{} - {}'.format(i._origin.element(), i._destination.element()))

    DFS(g, odd, {})