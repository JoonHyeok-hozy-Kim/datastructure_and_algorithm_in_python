<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 14
## 14.1 Graphs
#### Def.) Graph
* a graph G is simply a set V of vertices and a collection E of pairs of vertices from V, called edges.
* Components
  1. Edge (Arc)
  2. Vertex (Node)
  
<br>

#### Concepts) Terminologies related to Vertices and Edges
* **Directed vs Undirected**
  * directed edge
    * an edge that has order
  * undirected 
    * an edge that is not ordered 
* **Digraph and Mixed Graph**
  * Digraph
    * a graph that all edges are directed.
  * Mixed Graph
    * mixture of directed and undirected edges
* **Vertices Related**
  * end vertices (endpoints)
    * two vertices joined by an edge
  * origin of _e_
    * the first endpoint of a **directed edge _e_**
  * destination of _e_
    * the second endpoint of a **directed edge _e_**
* **Adjacent and Incident**
  * u, v are **adjacent** if there is an edge whose endpoints are u and v
  * An edge is **incident** to a vertex if the vertex is one of the edge's endpoints.
* **Edges Related**
   * outgoing edge of _v_
     * a directed edge whose origin is a vertex _v_
   * incoming edge of _v_
     * a directed edge whose destination is a vertex _v_
* **Degree**
  * deg(v) : degree of a vertex _v_
    * the number of incident edges of v
  * indeg(v) : in-degree of a vertex _v_
    * the number of incoming incident edges of v
  * outdeg(v) : out-degree of a vertex _v_
    * the number of outgoing incident edges of v
* **Parallel and Multiple Edge**
  * Edges to have same endpoints.
  * For directed edges, same origins and same destinations.
* **Self-Loop**
  * An edge whose two endpoints coincides.
* **Simple Graph**
  * A graph that does not have parallel or multiple edges
  * In this case the graph can also be called as a set, along with the more broad concept, collection.

<br>

#### Concept) Path and Cycle
* **Path**
  * a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each edge is incident to its predecessor and successor vertex
* **Cycle**
  * a path that starts and ends at the same vertex, and that includes at least one edge
* **Simplicity**
  * **Simple Path**
    * each vertex in the path is distinct 
  * **Simple Cycle**
    * each vertex in the cycle is distinct except for the first and last one.
* **Direct Path and Cycle**
  * all edges are directed and are traversed along their direction
* **Acyclic Graph**
  * A graph that has no directed cycles

<br>

#### Concept) Reachability, Connectedness, and Subgraph
* For a (directed) graph G and its vertices u and v, 
  * **"u reaches v" or "v is reachable from u"**
    * G has a (directed) path from u to v.
    * For an undirected graph, reachability is symmetric.
  * **"G is connected"**
    * There is a path between any two vertices of G.
  * **"Directed graph is strongly connected."**
    * For any two vertices u and v of G, u reaches v and v reaches u.
  * **Subgraph of a graph G**
    * a graph whose vertices and edges are subsets of the vertices and edges of G, respectively
  * **Spanning Subgraph of G** 
    * a subgraph of G that contains all the vertices of the graph G
  * **Connected Components of G**
    * G's maximal connected subgraphs if a graph G is not connected.

<br>

#### Concept) Forest and Tree
* **Forest**
  * A graph without cycles
* **Tree**
  * A connected forest, i.e., connected graph without cycles.
* **Spanning Tree of a graph**
  * a spanning subgraph that is a tree

<br>

#### Props.) 
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_01_01_graph_prop_1.png" style="width: 100%;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_01_01_graph_prop_2.png" style="width: 100%;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_01_01_graph_prop_3.png" style="width: 100%;"></img><br/>
</p>

* Justification
  * nC2 , nP2
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_01_01_graph_prop_4.png" style="width: 100%;"></img><br/>
</p>

### 14.1.1 The Graph ADT
#### Tech) Data types in a Graph
* Vertex
  * methods
    * element() : retrieve the stored element
* Edge
    * element() : retrieve the stored element
    * endpoints() : Return a tuple (u,v) such that vertex u is the origin of the edge and vertex v is the destination; for an undirected graph, the orientation is arbitrary.
    * opposite(v) : Assuming vertex v is one endpoint of the edge (either origin or destination), return the other endpoint.
* Graph
  * vertex count( ): Return the number of vertices of the graph.
  * vertices( ): Return an iteration of all the vertices of the graph.
  * edge_count( ): Return the number of edges of the graph.
  * edges( ): Return an iteration of all the edges of the graph.
  * get_edge(u,v): Return the edge from vertex u to vertex v, if one exists; otherwise return None. For an undirected graph, there is no difference between get edge(u,v) and get edge(v,u).
  * degree(v, out=True): For an undirected graph, return the number of edges incident to vertex v. For a directed graph, return the number of outgoing (resp. incoming) edges incident to vertex v, as designated by the optional parameter.
  * incident_edges(v, out=True): Return an iteration of all edges incident to vertex v. In the case of a directed graph, report outgoing edges by default; report incoming edges if the optional parameter is set to False.
  * insert_vertex(x=None): Create and return a new Vertex storing element x.
  * insert_edge(u, v, x=None): Create and return a new Edge from vertex u to vertex v, storing element x (None by default).
  * remove_vertex(v): Remove vertex v and all its incident edges from the graph.
  * remove_edge(e): Remove edge e from the graph.




## 14.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_08_exercises.md">Exercises</a>
