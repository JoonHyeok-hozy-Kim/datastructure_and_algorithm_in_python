<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md">Part 14. Graph Algorithms</a>
</p>

### R-14.1 Draw a simple undirected graph G that has 12 vertices, 18 edges, and 3 connected components.


### R-14.2 If G is a simple undirected graph with 12 vertices and 3 connected components, what is the largest number of edges it might have?


### R-14.3 Draw an adjacency matrix representation of the undirected graph shown in Figure 14.1.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_03_figure_14_1.png" style="height : 300px;"></img><br/>
</p>

* Sol.)
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_03_sol.png" style="height : 200px;"></img><br/>
</p>

### R-14.4 Draw an adjacency list representation of the undirected graph shown in Figure 14.1.
* Sol.)
```python
from DataStructures.graphs import Graph
v_src = [
    'Snoeyink',
    'Garg',
    'Goodrich',
    'Goldwasser',
    'Tamassia',
    'Tollis',
    'Vitter',
    'Preparata',
    'Chiang',
]
vertices = {}
g = Graph()
for name in v_src:
    vertices[name] = g.insert_vertex(name)
g.insert_edge(vertices['Snoeyink'], vertices['Goodrich'])
g.insert_edge(vertices['Goodrich'], vertices['Garg'])
g.insert_edge(vertices['Goodrich'], vertices['Goldwasser'])
g.insert_edge(vertices['Goodrich'], vertices['Tamassia'])
g.insert_edge(vertices['Goodrich'], vertices['Vitter'])
g.insert_edge(vertices['Goodrich'], vertices['Chiang'])
g.insert_edge(vertices['Tamassia'], vertices['Garg'])
g.insert_edge(vertices['Tamassia'], vertices['Goldwasser'])
g.insert_edge(vertices['Tamassia'], vertices['Tollis'])
g.insert_edge(vertices['Tamassia'], vertices['Vitter'])
g.insert_edge(vertices['Tamassia'], vertices['Preparata'])
g.insert_edge(vertices['Tamassia'], vertices['Chiang'])
g.insert_edge(vertices['Tollis'], vertices['Vitter'])
g.insert_edge(vertices['Vitter'], vertices['Preparata'])
g.insert_edge(vertices['Chiang'], vertices['Preparata'])

for v in g.vertices():
    print(v.element(), end=" - ")
    for e in g.incident_edges(v):
        print("[{}]".format(e), end= " ")
    print()
```
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_04_sol.png" style="width : 100%;"></img><br/>
</p>


### R-14.5 Draw a simple, connected, directed graph with 8 vertices and 16 edges such that the in-degree and out-degree of each vertex is 2. Show that there is a single (nonsimple) cycle that includes all the edges of your graph, that is, you can trace all the edges in their respective directions without ever lifting your pencil. (Such a cycle is called an Euler tour.)
* Sol.
```python
from DataStructures.graphs import Graph
g = Graph(True)
v = []
for i in range(8):
    v.append(g.insert_vertex(i))
for i in range(8):
    g.insert_edge(v[i], v[(i+1)%8])
    g.insert_edge(v[(i+1)%8], v[i])
for v in g.vertices():
    print('{} / out_degree : {} / in_degree : {}'.format(v, g.degree(v), g.degree(v, False)))
for v in g.vertices():
    print('{} : '.format(v), end="")
    for e in g.incident_edges(v):
        print(e, end=", ")
    print()
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_05_sol.png" style="height : 150px;"></img><br/>
</p>

### R-14.6 Suppose we represent a graph G having n vertices and m edges with the edge list structure. Why, in this case, does the insert vertex method run in O(1) time while the remove vertex method runs in O(m) time?
* Sol.)
  * Recall that edges are contained in an independent list.
  * Thus, insert_edge operation is simply appending new edge to the list, which takes O(1) time.
  * However, in case of the remove_edge operation, we should run a loop to search through the list to find the target edge.
    * This search will run in O(m) time in the worst case.

### R-14.7 Give pseudo-code for performing the operation insert edge(u,v,x)in O(1) time using the adjacency matrix representation.
* Sol.
```python
def insert_edge(u, v, x):
    Input : vertices u and v and element x for the edge
    Output : the edge instance

    i = self._item_idx(u)
    j = self._item_idx(v)
    self._data[i][j] = Edge(u, v, x)    
    if not self._is_directed:
        self._data[j][i] = Edge(u, v, x)
    return self._data[i][j]
```

### R-14.8 Repeat Exercise R-14.7 for the adjacency list representation, as described in the chapter.
* Sol.)
```python
def insert_edge(u, v, x):
    Input : vertices u and v and element x for the edge
    Output : the edge instance

    new_edge = Edge(u, v, x)
    self._edges.append(new_edge)    
    return new_edge
```

### R-14.9 Can edge list E be omitted from the adjacency matrix representation while still achieving the time bounds given in Table 14.1? Why or why not?
* Sol.) Yes. We can access the edges by traversing the matrix.

### R-14.10 Can edge list E be omitted from the adjacency list representation while still achieving the time bounds given in Table 14.3? Why or why not?
* Sol.) No. We may not be able to achieve O(m) time remove_edge, since we have to search all the vertices if E is omitted.

### R-14.11 Would you use the adjacency matrix structure or the adjacency list structure in each of the following cases? Justify your choice.
#### a. The graph has 10,000 vertices and 20,000 edges, and it is important to use as little space as possible.
* Sol.) Adjacency list may be appropriate. Edges are sparse and takes relatively little space compared to adjacency matrix.
#### b. The graph has 10,000 vertices and 20,000,000 edges, and it is important to use as little space as possible.
* Sol.) Adjacency matrix can be considered. 
  * Edges are quite densely populated. 
  * 10,000 vertices will generate 100,000,000 spaces for matrix and about 20% are being used.
#### c. You need to answer the query get edge(u,v) as fast as possible, no matter how much space you use.
* Sol.) Adjacency matrix is highly recommended. 
  * O(1) time is always guaranteed.

### R-14.12 Explain why the DFS traversal runs in O(n^2) time on an n-vertex simple graph that is represented with the adjacency matrix structure.
* Sol.) Adjacency matrix structure's incident_edges() method runs in O(n) time.
  * Thus, for each vertex on the path, the DFS will traverse through n elements in each row of the matrix.
  * Therefore, it runs in O(n^2) time.

### R-14.13 In order to verify that all of its nontree edges are back edges, redraw the graph from Figure 14.8b so that the DFS tree edges are drawn with solid lines and oriented downward, as in a standard portrayal of a tree, and with all nontree edges drawn using dashed lines.
* Sol.)
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_13_sol.png" style="height : 200px;"></img><br/>
</p>

### R-14.14 A simple undirected graph is complete if it contains an edge between every pair of distinct vertices. What does a depth-first search tree of a complete graph look like?
* Sol.) The DFS will be finished without running any loop. In other words, every vertex will have at most one parent and at most one child.

### R-14.15 Recalling the definition of a complete graph from Exercise R-14.14, what does a breadth-first search tree of a complete graph look like?
* Sol.) One vertex will be the only ancestor of every other vertices and these vertices will be leaves.

### R-14.16 Let G be an undirected graph whose vertices are the integers 1 through 8, and let the adjacent vertices of each vertex be given by the table below:


### R-14.17 Draw the transitive closure of the directed graph shown in Figure 14.2.


### R-14.18 If the vertices of the graph from Figure 14.11 are numbered as (v1 = JFK, v2 = LAX, v3 = MIA, v4 = BOS, v5 = ORD, v6 = SFO, v7 = DFW), in what order would edges be added to the transitive closure during the Floyd-Warshall algorithm?
* Sol.) 
  1. v3 - v6
  2. v3 - v7
  3. v4 - v6
  4. v4 - v7
  5. v3 - v5
  6. v1 - v2
  7. v1 - v5
  8. v2 - v4
  9. v2 - v6
  10. v4 - v5
  11. v5 - v6

### R-14.19 How many edges are in the transitive closure of a graph that consists of a simple directed path of n vertices?
* Sol) N = (n-1) + (n-2) + (n-3) + ... + 2 + 1 = (n-1)*n / 2


### R-14.20 Given an n-node complete binary tree T, rooted at a given position, consider a directed graph G having the nodes of T as its vertices. For each parent-child pair in T, create a directed edge in G from the parent to the child. Show that the transitive closure of G has O(nlogn) edges.
* Sol.)
* Test)
```python
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
    from DataStructures.tree import LinkedBinaryTree
    t = LinkedBinaryTree()
    t.fill_tree_height(4)
    print(t)
    transform = TreeGraphTransform(t)
    g = transform.execute()

    from GraphAlgorithms.transitive_closure import floyd_warshall
    c = floyd_warshall(g)
    print(len(c.edges()))
```

### R-14.21 Compute a topological ordering for the directed graph drawn with solid edges in Figure 14.3d.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_21_figure14_3_d.png" style="height : 300px;"></img><br/>
</p>

* Sol) TBS

### R-14.22 Bob loves foreign languages and wants to plan his course schedule for the following years. He is interested in the following nine language courses: LA15, LA16, LA22, LA31, LA32, LA126, LA127, LA141, and LA169.
* The course prerequisites
  * LA15: (none)
  * LA16: LA15
  * LA22: (none)
  * LA31: LA15
  * LA32: LA16, LA31
  * LA126: LA22, LA32
  * LA127: LA16
  * LA141: LA22, LA16
  * LA169: LA32
#### In what order can Bob take these courses, respecting the prerequisites?
* Sol.) (LA22) -> (LA15) -> (LA31) -> (LA16) -> (LA141) -> (LA127) -> (LA32) -> (LA169) -> (LA126)
```python
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
```

### R-14.23 Draw a simple, connected, weighted graph with 8 vertices and 16 edges, each with unique edge weights. Identify one vertex as a “start” vertex and illustrate a running of Dijkstra’s algorithm on this graph.
* Simulator
```python
from DataStructures.graphs import Graph
from GraphAlgorithms.depth_first_search import is_connected
from random import randint
g = Graph()
v = {}
weight_list = [i for i in range(16)]
for i in range(8):
    char = chr(i+65)
    v[char] = g.insert_vertex(char)
while not is_connected(g):
    g.truncate_edges()
    for i in range(16):
        rand_weight = weight_list.pop(randint(0, len(weight_list)-1)) if len(weight_list) > 1 else weight_list[0]
        x = y = None
        while x == y:
            x, y = v[chr(randint(0, 7)+65)], v[chr(randint(0, 7)+65)]
        g.insert_edge(x, y, rand_weight)

for e in g.edges():
    print('{} : {}'.format(e, e.element()))

from GraphAlgorithms.shortest_paths import dijkstra_shortest_path_lengths
random_start_vertex = v[chr(randint(0, 7)+65)]
print('Random Start : {}'.format(random_start_vertex))
cloud = dijkstra_shortest_path_lengths(g, random_start_vertex)
print('Dijkstra : ', end="")
for vertex in cloud:
    print(vertex, end=" > ")
```
* Sol.)
<div>
<div style="float : left">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_23_hand_sol.png" style="width : 35%"></img>
</div>
<div style="float : right">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_23_simulator_result.png" style="width : 35%"></img>
</div>
</div>






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md">Part 14. Graph Algorithms</a>
</p>