



if __name__ == '__main__':

    pass

    from DataStructures.graphs import Graph
    from DataStructures.graph_dfs import DFS, construct_path

    # g = Graph()
    # even = None
    # odd = None
    # for i in range(10):
    #     if i%2 == 0:
    #         even = g.insert_vertex(i)
    #         if odd is not None:
    #             g.insert_edge(odd, even)
    #     else:
    #         odd = g.insert_vertex(i)
    #         new_edge = g.insert_edge(even, odd)
    #
    # # for v in g.vertices():
    # #     print(v.element())
    # #
    # # for e in g.edges():
    # #     print('{} - {}'.format(e._origin.element(), e._destination.element()))
    # #
    # # for v in g.vertices():
    # #     print('Vertex : {}'.format(v.element()))
    # #     for i in g.incident_edges(v):
    # #         print('{} - {}'.format(i._origin.element(), i._destination.element()))
    #
    # discovered = {}
    # DFS(g, odd, discovered)
    # target = None
    # for k in discovered:
    #     if k.element() == 0:
    #         target = k
    # p = construct_path(odd, target, discovered)
    # # for v in p:
    # #     print('{} - '.format(v), end="")
    #
    # # a = next(iter(discovered.keys()))
    # # print(a.element())
    #
    # from DataStructures.graph_dfs import is_connected
    # print(is_connected(g))


    # Directed Graph
    g = Graph(True)
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

    from DataStructures.graph_dfs import DFS, is_connected, _incoming_DFS
    d = {}
    s = next(iter(g.vertices()))
    # print(s)
    DFS(g, s, d)
    print(len(d))

    # p = construct_path(s, odd, d)
    # for v in p:
    #     print('{} - '.format(v), end="")

    incoming_d = {}
    _incoming_DFS(g, s, incoming_d)
    # _incoming_edge_traversal(g, s, incoming_d)
    print(len(incoming_d))

    print(is_connected(g))


    g.insert_edge(odd, s)
    print(is_connected(g))