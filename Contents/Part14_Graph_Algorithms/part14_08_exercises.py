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


    from DataStructures.tree import LinkedBinaryTree
    t = LinkedBinaryTree()
    t.fill_tree_height(4)
    print(t)
    transform = TreeGraphTransform(t)
    g = transform.execute()

    from GraphAlgorithms.transitive_closure import floyd_warshall
    c = floyd_warshall(g)
    print(len(c.edges()))
