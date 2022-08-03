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
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_08_05_sol.png" style="height : 150px;"></img><br/>
</p>





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md">Part 14. Graph Algorithms</a>
</p>