from DataStructures.tree import BinaryEulerTour
from DataStructures.graphs import Graph
class TreeGraphTransform(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._graph = Graph()
        self._v = {}

    def execute(self):
        if len(self.tree()) > 0:
            self._tour(self._tree.root(), 0, [])
            return self._graph

    def _hook_previsit(self, p, d, path):
        e = p.element()
        self._v[e] = self._graph.insert_vertex(e)
        # print('In previsit : {}'.format(e))
        parent = self._tree.parent(p)
        if parent is not None:
            # print('{} - {}'.format(parent.element(), e))
            self._graph.insert_edge(self._v[parent.element()], self._v[e])


if __name__ == '__main__':
    pass

    # from DataStructures.graphs import Graph
    # v_src = [
    #     'Snoeyink',
    #     'Garg',
    #     'Goodrich',
    #     'Goldwasser',
    #     'Tamassia',
    #     'Tollis',
    #     'Vitter',
    #     'Preparata',
    #     'Chiang',
    # ]
    # vertices = {}
    # g = Graph()
    # for name in v_src:
    #     vertices[name] = g.insert_vertex(name)
    # g.insert_edge(vertices['Snoeyink'], vertices['Goodrich'])
    # g.insert_edge(vertices['Goodrich'], vertices['Garg'])
    # g.insert_edge(vertices['Goodrich'], vertices['Goldwasser'])
    # g.insert_edge(vertices['Goodrich'], vertices['Tamassia'])
    # g.insert_edge(vertices['Goodrich'], vertices['Vitter'])
    # g.insert_edge(vertices['Goodrich'], vertices['Chiang'])
    # g.insert_edge(vertices['Tamassia'], vertices['Garg'])
    # g.insert_edge(vertices['Tamassia'], vertices['Goldwasser'])
    # g.insert_edge(vertices['Tamassia'], vertices['Tollis'])
    # g.insert_edge(vertices['Tamassia'], vertices['Vitter'])
    # g.insert_edge(vertices['Tamassia'], vertices['Preparata'])
    # g.insert_edge(vertices['Tamassia'], vertices['Chiang'])
    # g.insert_edge(vertices['Tollis'], vertices['Vitter'])
    # g.insert_edge(vertices['Vitter'], vertices['Preparata'])
    # g.insert_edge(vertices['Chiang'], vertices['Preparata'])
    #
    # for v in g.vertices():
    #     print(v.element(), end=" - ")
    #     for e in g.incident_edges(v):
    #         print("[{}]".format(e), end= " ")
    #     print()


    # from DataStructures.graphs import Graph
    # g = Graph(True)
    # v = []
    # for i in range(8):
    #     v.append(g.insert_vertex(i))
    # for i in range(8):
    #     g.insert_edge(v[i], v[(i+1)%8])
    #     g.insert_edge(v[(i+1)%8], v[i])
    # for v in g.vertices():
    #     print('{} / out_degree : {} / in_degree : {}'.format(v, g.degree(v), g.degree(v, False)))
    # for v in g.vertices():
    #     print('{} : '.format(v), end="")
    #     for e in g.incident_edges(v):
    #         print(e, end=", ")
    #     print()


    # from DataStructures.tree import LinkedBinaryTree
    # t = LinkedBinaryTree()
    # t.fill_tree_height(4)
    # print(t)
    # transform = TreeGraphTransform(t)
    # g = transform.execute()
    #
    # from GraphAlgorithms.transitive_closure import floyd_warshall
    # c = floyd_warshall(g)
    # print(len(c.edges()))

    # from DataStructures.graphs import Graph
    # courses_list = [
    #     'LA15',
    #     'LA16',
    #     'LA22',
    #     'LA31',
    #     'LA32',
    #     'LA126',
    #     'LA127',
    #     'LA141',
    #     'LA169',
    # ]
    # g = Graph(True)
    # v = {}
    # for course in courses_list:
    #     v[course] = g.insert_vertex(course)
    #
    # g.insert_edge(v['LA15'], v['LA16'])
    # g.insert_edge(v['LA15'], v['LA31'])
    # g.insert_edge(v['LA16'], v['LA32'])
    # g.insert_edge(v['LA16'], v['LA127'])
    # g.insert_edge(v['LA16'], v['LA141'])
    # g.insert_edge(v['LA31'], v['LA32'])
    # g.insert_edge(v['LA22'], v['LA126'])
    # g.insert_edge(v['LA22'], v['LA141'])
    # g.insert_edge(v['LA32'], v['LA126'])
    # g.insert_edge(v['LA32'], v['LA169'])
    #
    # from SortingAlgorithms.topological_sort import topological_sort
    # g_sorted = topological_sort(g)
    # for v in g_sorted:
    #     print(v, end=" -> ")


    # from DataStructures.graphs import Graph
    # from GraphAlgorithms.depth_first_search import is_connected
    # from random import randint
    # g = Graph(True)
    # v = {}
    # for i in range(8):
    #     char = chr(i+65)
    #     v[char] = g.insert_vertex(char)
    # while not is_connected(g):
    #     # print('NOT connected')
    #     weight_list = [i for i in range(16)]
    #     g.truncate_edges()
    #     while len(weight_list) > 0:
    #         if len(weight_list) > 1:
    #             rand_weight = weight_list.pop(randint(0, len(weight_list)-1))
    #         else:
    #             rand_weight = weight_list.pop()
    #         x = y = None
    #         while x == y:
    #             x, y = v[chr(randint(0, 7)+65)], v[chr(randint(0, 7)+65)]
    #             if g.get_edge(x, y) is not None:
    #                 x = y = None
    #         g.insert_edge(x, y, rand_weight)
    #
    # for e in g.edges():
    #     print('{} : {}'.format(e, e.element()))
    #
    # from GraphAlgorithms.shortest_paths import dijkstra_shortest_path_lengths
    # random_start_vertex = v[chr(randint(0, 7)+65)]
    # print('Random Start : {}'.format(random_start_vertex))
    # cloud = dijkstra_shortest_path_lengths(g, random_start_vertex)
    # print('Dijkstra : ', end="")
    # for vertex in cloud:
    #     print(vertex, end=" > ")


    # from DataStructures.graphs import Graph
    # from GraphAlgorithms.depth_first_search import is_connected
    # from random import randint
    # g = Graph(True)
    # v = {}
    # for i in range(8):
    #     char = chr(i+65)
    #     v[char] = g.insert_vertex(char)
    # # print('NOT connected')
    # weight_list = [i for i in range(16)]
    # g.truncate_edges()
    # while len(weight_list) > 0:
    #     if len(weight_list) > 1:
    #         rand_weight = weight_list.pop(randint(0, len(weight_list)-1))
    #     else:
    #         rand_weight = weight_list.pop()
    #     x = y = None
    #     while x == y:
    #         x, y = v[chr(randint(0, 7)+65)], v[chr(randint(0, 7)+65)]
    #         if g.get_edge(x, y) is not None:
    #             x = y = None
    #     g.insert_edge(x, y, rand_weight)
    #
    # connected_v = []
    # for v in g.vertices():
    #     if is_connected(g, v):
    #         connected_v.append(v)
    #
    # if len(connected_v) > 0:
    #     for e in g.edges():
    #         print(e)
    #     for v in connected_v:
    #         print(v)
    #
    #     from GraphAlgorithms.shortest_paths import dijkstra_shortest_path_lengths
    #     s = connected_v.pop()
    #     print('Start : {}'.format(s))
    #     cloud = dijkstra_shortest_path_lengths(g, s)
    #     print('Dijkstra : ', end="")
    #     for vertex in cloud:
    #         print(vertex, end=" > ")

    from DataStructures.graphs import Graph
    from GraphAlgorithms.depth_first_search import is_connected
    from random import randint
    g = Graph()
    v = {}
    for i in range(8):
        char = chr(i+65)
        v[char] = g.insert_vertex(char)
    while not is_connected(g):
        # print('NOT connected')
        weight_list = [i for i in range(16)]
        g.truncate_edges()
        while len(weight_list) > 0:
            if len(weight_list) > 1:
                rand_weight = weight_list.pop(randint(0, len(weight_list)-1))
            else:
                rand_weight = weight_list.pop()
            x = y = None
            while x == y:
                x, y = v[chr(randint(0, 7)+65)], v[chr(randint(0, 7)+65)]
                if g.get_edge(x, y) is not None:
                    x = y = None
            g.insert_edge(x, y, rand_weight)

    for e in g.edges():
        print('{} : {}'.format(e, e.element()))

    from GraphAlgorithms.minimum_spanning_tree import MST_PrimJarnik
    tree = MST_PrimJarnik(g)
    for edge in tree:
        print(edge)
