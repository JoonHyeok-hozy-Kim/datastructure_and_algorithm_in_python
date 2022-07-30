


if __name__ == '__main__':

    from DataStructures.graphs import Graph
    from SortingAlgorithms.topological_sort import topological_sort

    g = Graph(True)

    # Insert vertices and append them to a list for convenience
    vertices_list = []
    for i in range(8):
        u = g.insert_vertex(chr(i+65))
        vertices_list.append(u)

    # Insert edges
    g.insert_edge(vertices_list[0], vertices_list[2])
    g.insert_edge(vertices_list[0], vertices_list[3])
    g.insert_edge(vertices_list[1], vertices_list[3])
    g.insert_edge(vertices_list[2], vertices_list[4])
    g.insert_edge(vertices_list[1], vertices_list[5])
    g.insert_edge(vertices_list[3], vertices_list[5])
    g.insert_edge(vertices_list[4], vertices_list[6])
    g.insert_edge(vertices_list[5], vertices_list[6])
    g.insert_edge(vertices_list[5], vertices_list[7])
    g.insert_edge(vertices_list[6], vertices_list[7])

    l = topological_sort(g)
    for v in l:
        print(v)