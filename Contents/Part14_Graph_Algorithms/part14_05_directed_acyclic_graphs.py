


if __name__ == '__main__':

    # from DataStructures.graphs import Graph
    # from SortingAlgorithms.topological_sort import topological_sort
    #
    # g = Graph(True)
    #
    # # Insert vertices and append them to a list for convenience
    # vertices_list = []
    # for i in range(8):
    #     u = g.insert_vertex(chr(i+65))
    #     vertices_list.append(u)
    #
    # # Insert edges
    # g.insert_edge(vertices_list[0], vertices_list[2])
    # g.insert_edge(vertices_list[0], vertices_list[3])
    # g.insert_edge(vertices_list[1], vertices_list[3])
    # g.insert_edge(vertices_list[2], vertices_list[4])
    # g.insert_edge(vertices_list[1], vertices_list[5])
    # g.insert_edge(vertices_list[3], vertices_list[5])
    # g.insert_edge(vertices_list[4], vertices_list[6])
    # g.insert_edge(vertices_list[5], vertices_list[6])
    # g.insert_edge(vertices_list[5], vertices_list[7])
    # g.insert_edge(vertices_list[6], vertices_list[7])
    #
    # l = topological_sort(g)
    # for v in l:
    #     print(v)


    ''' Monte Carlo Simulation '''
    from random import randrange
    n = 300
    digit = 10
    normalizing = pow(10, digit)
    in_cnt = 0
    out_cnt = 0
    for i in range(n):
        x = randrange(normalizing*(-1), normalizing) / normalizing
        y = randrange(normalizing*(-1), normalizing) / normalizing
        # print(x, y, x*x + y*y)
        if x*x + y*y <= 1:
            # print('in')
            in_cnt += 1
        else:
            # print('out')
            out_cnt += 1
    result = 4 * in_cnt / n
    print(result)