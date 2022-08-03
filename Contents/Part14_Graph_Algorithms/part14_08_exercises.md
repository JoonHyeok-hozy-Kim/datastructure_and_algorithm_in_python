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

### 











<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md">Part 14. Graph Algorithms</a>
</p>