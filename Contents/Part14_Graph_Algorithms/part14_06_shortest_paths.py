



if __name__ == '__main__':

    pass

    # from DataStructures.priority_queues import LocationAwareUnsortedPriorityQueue
    # from random import randint
    # pq = LocationAwareUnsortedPriorityQueue()
    # for i in range(5):
    #     n = randint(1, 100)
    #     pq.add(n, n)
    #     print("{} added.".format(n))
    #     print("min : {}".format(pq.min()))

    from DataStructures.graphs import Graph
    from GraphAlgorithms.shortest_paths import dijkstra_shortest_path_lengths

    g = Graph()
    v_list = ['BOS', 'PVD', 'JFK', 'BWI', 'ORD', 'SFO', 'LAX', 'DFW', 'MIA']
    e_list = [
        ['BOS', 'SFO', 2704],
        ['BOS', 'ORD', 867],
        ['BOS', 'JFK', 187],
        ['BOS', 'MIA', 1258],
        ['PVD', 'ORD', 849],
        ['PVD', 'JFK', 144],
        ['ORD', 'SFO', 1846],
        ['ORD', 'DFW', 802],
        ['ORD', 'JFK', 740],
        ['ORD', 'BWI', 621],
        ['JFK', 'DFW', 1391],
        ['JFK', 'BWI', 184],
        ['BWI', 'MIA', 946],
        ['DFW', 'SFO', 1464],
        ['DFW', 'LAX', 1235],
        ['DFW', 'MIA', 1121],
        ['SFO', 'LAX', 337],
        ['LAX', 'MIA', 2342],
    ]
    v_dict = {}

    for v in v_list:
        vertex = g.insert_vertex(v)
        v_dict[v] = vertex

    for e in e_list:
        u = v_dict[e[0]]
        v = v_dict[e[1]]
        g.insert_edge(u, v, e[2])

    from GraphAlgorithms.depth_first_search import DFS, construct_path
    d = {}
    DFS(g, v_dict['BOS'], d)
    path_dfs = construct_path(v_dict['BOS'], v_dict['LAX'], d)
    print('---DFS---')
    for v in path_dfs:
        print(v)

    from GraphAlgorithms.breadth_first_search import BFS
    b = {}
    BFS(g, v_dict['BOS'], b)
    path_bfs = construct_path(v_dict['BOS'], v_dict['LAX'], b)
    print('---BFS---')
    for v in path_bfs:
        print(v)

    print('---Shortest Path---')
    from GraphAlgorithms.shortest_paths import dijkstra_shortest_path_lengths
    cloud = dijkstra_shortest_path_lengths(g, v_dict['BWI'])
    for c in cloud:
        print('{} : {}'.format(c, cloud[c]))

    print('---Shortest Path Tree---')
    from GraphAlgorithms.shortest_paths import shortest_path_tree
    tree = shortest_path_tree(g, v_dict['BOS'], cloud)
    for v in tree:
        print('{} / {}'.format(v, tree[v]))