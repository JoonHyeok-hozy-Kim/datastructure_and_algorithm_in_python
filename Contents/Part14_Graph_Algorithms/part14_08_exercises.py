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

    from DataStructures.graphs import Graph
    courses_list = [
        'LA15',
        'LA16',
        'LA22',
        'LA31',
        'LA32',
        'LA126',
        'LA127',
        'LA141',
        'LA169',
    ]
    g = Graph(True)
    v = {}
    for course in courses_list:
        v[course] = g.insert_vertex(course)

    g.insert_edge(v['LA15'], v['LA16'])
    g.insert_edge(v['LA15'], v['LA31'])
    g.insert_edge(v['LA16'], v['LA32'])
    g.insert_edge(v['LA16'], v['LA127'])
    g.insert_edge(v['LA16'], v['LA141'])
    g.insert_edge(v['LA31'], v['LA32'])
    g.insert_edge(v['LA22'], v['LA126'])
    g.insert_edge(v['LA22'], v['LA141'])
    g.insert_edge(v['LA32'], v['LA126'])
    g.insert_edge(v['LA32'], v['LA169'])

    from SortingAlgorithms.topological_sort import topological_sort
    g_sorted = topological_sort(g)
    for v in g_sorted:
        print(v, end=" -> ")

