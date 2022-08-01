

if __name__ == '__main__':

    from DataStructures.graphs import Graph
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

    from GraphAlgorithms.minimum_spanning_tree import MST_PrimJarnik
    tree = MST_PrimJarnik(g)
    # print(tree)
    for e in tree:
        print(e)