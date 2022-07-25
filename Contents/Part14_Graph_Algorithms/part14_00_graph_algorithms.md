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



## 14.2 Data Structures for Graphs
#### Tech.) Comparing 4 ways to maintain collection of vertices in a graph
1. Edge List
   * Maintain an unordered list of all edges.
   * No efficient way to locate a particular edge (u, v)
   * No efficient way to locate the set of all edges incident to  a vertex v.
2. Adjacency List
   * Maintain a separate list for each vertex containing those edges that are incident to the vertex.
   * The complete set of edges can be determined by taking the union of the smaller sets.
   * Efficient in finding all edges incident to a given vertex.
3. Adjacency Map
   * Similar to Adjacency List.
   * Use Map as a container instead of the list.
   * Allows O(1) expected time access to a specific edge (u, v).
4. Adjacency Matrix
   * Maintain an n X n matrix, for a graph with n vertices.
   * Provides worst-case O(1) access to a specific edge (u,v)
   * Each entry is dedicated to storing a reference to the edge (u,v) for a particular pair of vertices u and v.
     * If no such edge exists, the entry will be None.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_02_02_edge_list_image.png" style="width: 100%;"></img><br/>
</p>

### 14.2.1 Edge List Structure
#### Tech) Structure
* V : an unordered list that stores all vertex objects
  * The vertex object for a vertex v storing element x has instance variables for:
    * A reference to element x, to support the element() method.
    * A reference to the position of the vertex instance in the listV, thereby allowing v to be efficiently removed from V if it were removed from the graph.
* E : an unordered list that stores all edge objects
  * The edge object for an edge e storing element x has instance variables for:
    * A reference to element x, to support the element( ) method.
    * References to the vertex objects associated with the endpoint vertices of e. 
        * These allow the edge instance to provide constant-time support for methods endpoints( ) and opposite(v).
    * A reference to the position of the edge instance in list E, thereby allowing e to be efficiently removed from E if it were removed from the graph.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_02_01_comparison_between_various_graph_maintanence.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Performance
* For n vertices and m edges...
  * Space Usage trivially O(m+n)
  * vertex_count and edge_count trivially O(1)
  * Edge related operations : O(m)
    * get edge(u,v), degree(v), and incident edges(v).
    * Must run through all the elements in E in order to search the target edge.
  * insert_vertex() and insert_edge in O(1)
    * Simply appending element to V and E respectively.
  * remove_edge(e) in O(1)
    * Simply removing an edge.
  * remove_vertext(v) in O(m)
    * why?)
      * We need to search edges whose endpoint is v.


### 14.2.2 Adjacency List Structure
#### Tech) Structure
* V : the collection of vertices.
  * Represented by a PositionalList of vertices.
  * Each element v maintains a direct reference to its I(v) below.
* For each vertex v, we maintain a collection I(v), called the incidence collection of v, whose entries are edges incident to v.
  * In the case of a directed graph, outgoing and incoming edges can be respectively stored in two separate collections, I_out(v) and I_in(v).
  * Traditionally, I(v) for a vertex v is a list.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_02_03_adjacency_list_image.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Advantage of Adjacency List
* incident_edges(v) can be directly called from the vertex v
  * the iteration may run in O(deg(v)) times.

#### Analysis) Performance of the Adjacency List Structure
* For n vertices and m edges...
  * Space Usage : O(m+n)
    * why?
      1. n vertices take O(n) space.
      2. m vertices may be contained in vertices constant times. (Recall that n*(n-1) for directed graph and n*(n-1)/2 for undirected graph.)
  * incident_edges(v) in O(deg(v)) time.
    * Justified above.
  * degree(v) trivially in O(1) time.
  * get_edge(u, v) in O( min{deg(u), deg(v)} ) time.
    * By choosing a vertex with smaller I() we can reduce the running time.


### 14.2.3 Adjacency Map Structure
#### Tech.) Structure
* Use a hash-based map to implement I(v) for each vertex v.
* Let the **opposite endpoint** of each incident edge serve as a key in the map.


#### Analysis) Performance of the Adjacency List Structure
* For n vertices and m edges...
  * Space Usage : O(m+n)
    * why?
      * I(v) uses O(deg(v)) space for each vertex v, as with the adjacency list.
  * get_edge(u,v) in expected O(1) time 
    * why?
      * We can search for vertex u as a key in I(v) in O(1) time with hash-based map.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_02_04_adjacency_map_image.png" style="width: 100%;"></img><br/>
</p>


### 14.2.4 Adjacency Matrix Structure
#### Tech) Structure
* Augments the edge list structure with a matrix A (a.k.a. 2 dimensional array)
  * It allows us to locate an edge between a given pair of vertices in worst-case constant time.
  * For u and v with index i and j respectively, the cell A[i, j] holds a reference to the edge (u,v), if it exists.
    * A[i, j] = None if there is no such edge
    * A is symmetric if graph G is undirected, i.e., A[i, j] == A[j, i]

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_02_05_adjacency_matrix_image.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Advantages and Disadvantage of the Adjacency Matrix Structure
* Advantage
  * Any edge (u,v) can be accessed in worst-case O(1) time
    * Still, to find the edges incident to vertex v, we must presumably examine all n entries in the row associated with v.
* Disadvantage
  * Adding or removing vertices from a graph is problematic, as the matrix must be resized.
  * O(n2) space usage.
    * Recall O(m+n) for others.
  * Most real-world graphs are sparse.
    * which means that most of the elements of the matrix A will be None.
    * Very inefficient.


### 14.2.5 Python Implementation
* Structure
  * A variant of the **adjacency map**
    * For each vertex v, we use a Python dictionary to represent the secondary incidence map I(v).
    * However, we do not explicitly maintain lists V and E.
      * The list V is replaced by a top-level dictionary D that maps each vertex v to its incidence map I(v).
        * By doing this we need not maintain references to those incidence maps as part of the vertex structures.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graphs.py#L37">Graph</a>
* Analysis
  * Some of the worst-case running time bounds for the graph ADT operations become expected bounds.
    * ex.) edges()
      * It may run in O(n+m) time.
      * why?)
        * We might have to go through all the vertices in order to find the union of all the edges.
        * Moreover, some vertices may not even incident with an edge.


## 14.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_08_exercises.md">Exercises</a>
