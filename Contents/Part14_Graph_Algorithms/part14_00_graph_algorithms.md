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

---

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

---

## 14.3 Graph Traversals
#### Def.) Traversal
* A systematic procedure for exploring a graph by examining all of its vertices and edges.

#### Concept) Problems related to Reachability
* Computing a path from vertex u to vertex v, or reporting that no such path exists.
* Given a start vertex s of G, computing, for every vertex v of G, a path with the minimum number of edges between s and v, or reporting that no such path exists.
* Testing whether G is connected.
* Computing a spanning tree of G, if G is connected.
* Computing the connected components of G.
* Computing a cycle in G, or reporting that G has no cycles.

#### Concept) Problems related to Reachability in a Directed Graph G
* Computing a directed path from vertex u to vertex v, or reporting that no such path exists.
* Finding all the vertices of G that are reachable from a given vertex s.
* Determine whether G is acyclic.
* Determine whether G is strongly connected.


### 14.3.1 Depth-First Search (DFS)
* How?
  1. We begin at a specific starting vertex s in G, which we initialize by fixing one end of our string to s and painting s as “visited.”
     * Let u denote the current vertex. For now, u = s.
  2. We then traverse G by considering an (arbitrary) edge (u,v) incident to the current vertex u.
  3. If (u,v) leads to an unvisited vertex v, then we unroll our string, and go to v.
     * Else if the edge (u,v) leads us to a vertex v that is already visited, we ignore that edge.
  4. Eventually, we will get to a “dead end,” that is, a current vertex v such that all the edges incident to v lead to vertices already visited.
  5. Go back to previous vertex and repeat from 2.
  6. The process terminates when our backtracking leads us back to the start vertex s, and there are no more unexplored edges incident to s.

#### Tech.) Pseudo Code for DFS
```python
Algorithm DFS(G, u):
    Input : A graph G and a vertex u of G
    Output : A collection of vertices reachable from u with their discovery edges
    for each outgoing edge e = (u,v) of u do
        if vertex v has not been visited then
            Mark vertex v as visited (via edge e)
            Recursively call DFS(G, v)
```

#### Tech.) Depth-First Search Tree : Classifying Graph Edges with DFS
* Props.)
  * Rooted at a starting vertex s
* Concepts)
  * Discovery Edge or Tree Edge
    * An edge e = (u,v) that is used to discover a new vertex v during the DFS algorithm
  * Nontree Edge
    * All edges that are not Tree Edges
    * They take us to a previously visited vertex.
  * Back / Forward / Cross Edge
    * Back Edge : Connects a vertex to an ancestor in the DFS tree
    * Forward Edge : Connects a vertex to a descendant in the DFS tree
    * Cross Edge : Connects a vertex to a vertex that is neither its ancestor nor its descendant.


#### Props.) Properties of a Depth-First Search
* Prop.) Let G be an undirected graph on which a DFS traversal starting at a vertex s has been performed. 
  * Then the traversal visits all vertices in the connected component of s, and the discovery edges form a spanning tree of the connected component of s.
    * Justification
      * Suppose there is at least one vertex w in s’s connected component not visited.
      * Let v be the first unvisited vertex on some path from s to w.
        * Then we may have v = w.
      * Since v is the first unvisited vertex on this path, it has a neighbor u that was visited.
      * But when we visited u, we must have considered the edge (u,v).
      * Hence, it cannot be correct that v is unvisited. ---> (X)
      * Therefore, there are no unvisited vertices in s’s connected component.

* Prop.) In DFS, the discovery edges form a connected subgraph without cycles, hence a tree.
  * Justification
    * We only follow a discovery edge when we go to an unvisited vertex, we will never form a cycle with such edges.

* Prop.) For a directed graph G, Depth-first search on G starting at a vertex s visits all the vertices of G that are reachable from s. 
  * Justification
    * Let V_s be the subset of vertices of G visited by DFS starting at vertex s.
    * We want to show that V_s contains s and every vertex reachable from s belongs to V_s.
    * Suppose now, for the sake of a contradiction, that there is a vertex w reachable from s that is not in V_s.
    * Consider a directed path from s to w, and let (u,v) be the first edge on such a path taking us out of V_s. 
      * i.e., u is in V_s but v is not in V_s.
    * When DFS reaches u, it explores all the outgoing edges of u, and thus must reach also vertex v via edge (u,v).
    * Hence, v should be in V_s. ---> (X)
    * Therefore, V_s must contain every vertex reachable from s.

* Prop.) DFS tree contains directed paths from s to every vertex reachable from s.
  * Justification
    * Let u and v, vertices reachable from s and they are outpoints of an edge e.
    * u must have previously been discovered, there exists a path from s to u.
    * By appending the edge (u,v) to that path, we have a directed path from s to v.

* Prop.) A cycle in G, consisting of the discovery edges from u to v, also contains the back edge (u,v).
  * Justification
    * Back edges always connect a vertex v to a previously visited vertex u


#### Analysis) Running Time of Depth-First Search
* Let
  * n_s : the number of vertices reachable from a vertex s
  * m_s : the number of incident edges to those vertices
* Then the DFS starting from s runs in O(n_s + m_s) time.
* Under the assumption that the following conditions are satisfied.
  1. The graph is represented by a data structure such that creating and iterating through the incident_edges(v) takes O(deg(v)) time, and the e.opposite(v) method takes O(1) time.
     * Applicable : Adjacency List
     * Not Applicable : Adjacency Matrix
  2. We have a way to “mark” a vertex or edge as explored, and to test if a vertex or edge has been explored in O(1) time.


#### Analysis) Running Time of DFS applications
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_03_04_dfs_applicaiton_running_time.png" style="width: 100%;"></img><br/>
</p>


### 14.3.2 DFS Implementation and Extensions
* Implementation : [Depth First Search (DFS)](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/depth_first_search.py)


#### Concept) The existences of the dictionary, **discovered**, as an input parameter for DFS
* Purpose
  1. Internally, the dictionary provides a mechanism for recognizing visited vertices, as they will appear as keys in the dictionary.
  2. Externally, the DFS function augments this dictionary as it proceeds, and thus the values within the dictionary are the DFS tree edges at the conclusion of the process.
* Drawback
  * The dictionary data type that we used may run in **expected** O(1) time for a search, discovered[v] = e
    * Rather than the worst-case time.
    * It can be a violation to the property that we defined before. (Check the [Assumption](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md#analysis-running-time-of-depth-first-search))


#### Tech.) Reconstructing a Path from u to v
* Implementation : [construct_path(u, v, discovered)](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/depth_first_search.py#L17)
* Performance
  * Running time proportional to the length of the path
    * Thus, it runs in O(n) time.


#### Tech.) Testing the Connectivity of a Undirected Graph
* How?
  1. Choose an arbitrary vertex as a start.
  2. Operate DFS search.
  3. Compare len(discovered) and the number of vertices.
* Result
  * If len(discovered) == len(g._outgoing), then g is connected.
  * Else, g is not connected.
* Implementation : [is_connected?](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/depth_first_search.py#L17)


#### Tech.) Testing the Strong Connectivity of a Directed Graph
* How?
  * Choose an arbitrary vertex as a start.
  * Operate DFS search.
    * If there exists a vertex that is not visited, this graph is not strongly connected.
  * Now we have to check whether s is reachable from all other vertices.
    * With the DFS method, loop through all incoming edges to the current vertex.
      * This will run in O(m+n) time.
* Implementation : [is_connected for indirect graph](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/depth_first_search.py#L38)


#### Tech.) Computing all Connected Components
* Target
  * For a not connected graph, we will identify 
    * all of the connected components of an undirected graph
    * the strongly connected components of a directed graph.
* How?
  * If an initial call to DFS fails to reach all vertices of a graph, we can restart a new call to DFS at one of those unvisited vertices.
* Implementation : [DFS_complete](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/depth_first_search.py#L65)
* Performance
  * The total time spent by a call to DFS complete is **O(n+m)**.
    * Why?)
      * Recall that single DFS starting from s runs in O(n_s + m_s) time.
        * n_s : the number of reachable vertices
        * m_s : the number of incident edges to those vertices
      * If certain vertex is already discovered during the previous DFS, a DFS starting from it will be skipped!


#### Tech.) Detecting Cycles with DFS
* Prop.) For both undirected and directed graphs, a cycle exists if and only if a back edge exists relative to the DFS traversal of that graph.



### 14.3.3 Breadth-First Search
#### Tech.) Structure
* How?
  * A BFS proceeds in rounds and subdivides the vertices into levels.
    1. BFS starts at vertex s, which is at level 0.
    2. In the first round, we paint as “visited,” all vertices adjacent to the start vertex s.
       * These adjacent vertices are actually level 1 but not being painted.
    3. In the second round, we allow all explorers to go two steps (i.e., edges) away from the starting vertex.
       * Assign these vertices to level 2 and mark them as visited.
    4. Continue this process until no new vertices are found in a level.

#### Implementation : [Breadth First Search (BFS)](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/breadth_first_search.py)

#### Analysis) Performance of BFS
* The running time of BFS is O(n + m)
  * More specifically, in O(n_s + m_s) time
    * n_s : the number of vertices reachable from vertex s
    * ms ≤ m : the number of incident edges to those vertices.

#### Props.)
* Prop.) For BFS on an undirected graph, all nontree edges are cross edges.
* Prop.) For BFS on a directed graph, all nontree edges are either back edges or cross edges

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_03_05_bfs_prop_1.png" style="width: 100%;"></img><br/>
</p>

* Prop.) Let G be a graph with n vertices and m edges represented with the adjacency list structure. A BFS traversal of G takes O(n+m) time.

---

## 14.4 Transitive Closure
* Idea
  * In certain applications, we may wish to answer many reachability queries more efficiently.
  * It may be worthwhile to precompute a more convenient representation of a graph.

#### Def.) Transitive Closure
* The transitive closure of a directed graph G is itself a directed graph G∗ such that the vertices of G∗ are the same as the vertices of G , and G∗ has an edge (u,v), whenever G has a directed path from u to v (including the case where (u,v) is an edge of the original G).
* Prop.)
  * If a graph is represented as an adjacency list or adjacency map, we can compute its transitive closure in O(n(n+m)) time.
    * By making use of n graph traversals, one from each starting vertex.
  * We want to figure out alternative and more efficient techniques for computing the transitive closure.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_01_transitive_closure_prop.png" style="width: 100%;"></img><br/>
</p>

#### Tech.) Floyd-Warshall algorithm
* Pseudo Code
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_02_floyd_warshal_pseudo_code.png" style="heigth: 400px;"></img><br/>
</p>

* Performance
  * Assume that get_edge and insert_edge of G run in O(1) times.
  * Floyd-Warshall algorithm runs in O(n^3) time.
    * why?
      * Outer for-loop runs in O(n) time.
      * Inner for-loop for i and j runs in O(n) time respectively.
  * Floyd-Warshall algorithm matches asymptotic bounds in following two cases.
    1. The graph is dense
    2. The graph is sparse but represented as an adjacency matrix.

* Prop.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_03_floyd_warshal_prop.png" style="width: 100%"></img><br/>
</p>

#### Floyd-Warshall algorithm Simulation
1. For the vertex v1
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_04_floyd_warshal_simulation_v1.png" style="height: 300px;"></img><br/>
</p>

2. For the vertex v3
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_04_floyd_warshal_simulation_v3.png" style="height: 300px;"></img><br/>
</p>

3. For the vertex v4
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_04_floyd_warshal_simulation_v4.png" style="height: 300px;"></img><br/>
</p>

4. For the vertex v5
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_04_04_floyd_warshal_simulation_v5.png" style="height: 300px;"></img><br/>
</p>

* Pros and Cons of Floyd-Warshall algorithm
  * Advantage
    * Easier to implement than DFS
    * Faster in practice because there are relatively few low-level operations hidden within the asymptotic notation
    * Well suited for the use of an adjacency matrix
  * Disadvantage
    * Repeated calls to DFS results in better asymptotic performance when the graph is sparse and represented using an adjacency list or adjacency map.

#### Python Implementation : [Floyd-Warshall Algorithm](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/transitive_closure.py)

---

## 14.5 Directed Acyclic Graphs
#### Def.) Directed Acyclic Graph (DAG)
  * A Directed graph without directed cycles are encountered in many applications

### 14.5.1 Topological Ordering
#### Def.) Topological Ordering
* For a directed graph G with n vertices
  * A topological ordering of G is an ordering v1,...,vn of the vertices of G such that for every edge (vi,vj) of G , it is the case that i < j.
  * i.e., an ordering such that any directed path in G traverses vertices in increasing order.

#### Props.)
* Prop.) A directed graph may have more than one topological ordering.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_05_01_multiple_topological_ordering_in_one_graph.png" style="width: 100%;"></img><br/>
</p>

* Prop.)
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_05_02_topological_ordering_prop.png" style="width: 100%;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_05_03_topological_ordering_prop_pf.png" style="width: 100%;"></img><br/>
</p>


#### Tech.) Topological Sorting
* Implementation : [Topological Sorting](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/topological_sort.py)
* Performance
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_05_04_topological_sorting_performance.png" style="width: 100%;"></img><br/>
</p>

* Test
```python
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
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_05_05_topological_sorting_test.png" style="height : 300px;"></img><br/>
</p>

---
<br>


## 14.6 Shortest Paths
* We want to consider the case tha each edge has different value and path finding algorithms that take it into account.

### 14.6.1 Weighted Graphs
* Def.) A weighted graph is a graph that has a numeric (for example, integer) label w(e) associated with each edge e, called the weight of edge e.
  * For e = (u,v), we let notation w(u,v) = w(e).

#### Concept) Defining Shortest Paths in a Weighted Graph
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_06_01_definitions_for_weighted_graphs.png" style="width: 100%;"></img><br/>
</p>

#### Notation) d(u,v)
* the distance between u and v
* "d(u,v) = ∞" : There is no path at all from u to v in G.

#### Prop.) If there is a cycle in G whose total weight is negative, the distance from u to v may not be defined.
* ex.) Let the weight of edge as the cost spent for moving from one airport to another.
  * If someone else pays not charges for the trip from JFK to LAX, we cannot define the cheapest root.
    * why?
      * One may infinitely reduce cost by continuously oscillate between JFK and LAX.


### 14.6.2 Dijkstra’s Algorithm
* Concepts)
  * We will apply greedy method pattern to the single-source-shortest path problem.
    * by performing a “weighted” breadth-first search starting at the source vertex s.
  * We can use the greedy method to develop an algorithm that iteratively grows a “cloud” of vertices out of s, with the vertices entering the cloud in order of their distances from s.
    * in each iteration, the next vertex chosen pis the vertex outside the cloud that is closest to s.
  * The algorithm terminates when no more vertices are outside the cloud (or when those outside the cloud are not connected to those within the cloud), at which point we have a shortest path from s to every vertex of G that is reachable from s.


#### Concept) Edge Relaxation
* For a graph G, starting vertex s
  * Let
    * D[v]
      * the distance in G from s to a vertex v
      * always store the length of the best path we have found so far from s to v
      * Initially,
        * D[s] = 0
        * D[v] = ∞ for each v != s
    * C
      * the cloud of vertices
  * At each iteration of the algorithm, 
    1. Select a vertex u not in C with smallest D[u] label, 
    2. Pull u into C
    3. Update the label D[v] of each vertex v that is adjacent to u and is outside of C
       * Reflect the fact that there may be a new and better way to get to v via u.
       * This update operation is known as a **relaxation** procedure

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_06_02_edge_relaxation.png" style="height : 150px;"></img><br/>
</p>

* Pseudo Code
```python
Algorithm ShortestPath(G, s):
  Input: A weighted graph G with nonnegative edge weights, and a distinguished   vertex s of G.
  Output: The length of a shortest path from s to v for each vertex v of G.
  
  Initialize D[s] = 0 and D[v] = ∞ for each vertex v != s.
  Let a priority queue Q contain all the vertices of G using the D labels as keys.
  while Q is not empty do
    {pull a new vertex u into the cloud}
    u = value returned by Q.remove_min()
    for each vertex v adjacent to u such that v is in Q do
      {perform the relaxation procedure on edge (u,v)}
      if D[u] + w(u,v) < D[v] then
        D[v] = D[u] + w(u,v)
        Change to D[v] the key of vertex v in Q.
  return the label D[v] of each vertex v
```

<br>

#### Prop.) In Dijkstra’s algorithm, whenever a vertex v is pulled into the cloud, the label D[v] is equal to d(s,v), the length of a shortest path from s to v.
* Justification : Proof by contradiction
  * Suppose that D[v] > d(s,v) for some vertex v in V.
    * i.e.) D[v] calculated by Dijkstra's algorithm is not the shortest path!
    * Let z be _the first vertex_ the algorithm pulled into the cloud C such that D[z] > d(s,z).
  * Then there is a shortest path P from s to z (for otherwise d(s,z) = ∞ = D[z]).
    * Let us therefore consider the moment when z is pulled into C.
    * Let y be the first vertex of P (when going from s to z) that is not in C at this moment.
    * Let x be the predecessor of y in path P.
      * By our choice of y, that x is already inC at this point.
      * D[x] = d(s,x), since z is _the first incorrect vertex._
        * Then, D[y] ≤ D[x] +w(x,y) = d(s,x) + w(x,y).
    * But since y is the next vertex on the shortest path from s to z, this implies that
      * D[y] = d(s,y).
    * But we are now at the moment when we are picking z, not y, to join C; hence,
      * D[z] ≤ D[y].
    * Since y is on the shortest path from s to z,
      * d(s,y) + d(y,z) = d(s,z).
    * Therefore,
      * D[z] ≤ D[y] = d(s,y) ≤ d(s,y) +d(y,z) = d(s,z) ---> (X)


<br>

#### Analysis) The Running Time of Dijkstra’s Algorithm
* Assumptions
  * Let 
    * G : a graph G with n vertices and m edges
    * The edge weights can be added and compared in constant time.
* Choosing priority_queue Q data structure
  1. [AdaptablePriorityQueue](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L191)
     * Advantage
       * O(log(n)) time remove_min() operation.
         * Thus, n calls to the remove_min : O(n log(n))
     * Disadvantage
       * O(log(n)) time for following operations
         1. Initial n insertions to Q : O(n log(n))
         2. m calls to update method : O(m log(n))

  2. [UnsortedPriorityQueue](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L265)
     * Advantage
       * Under the assumption that Q supports location-aware entries...
         1. Initial n insertions to Q : O(n)
         2. m calls to update method : O(m)
     * Disadvantage
       * O(n) time remove_min() operation.
         * Thus, n calls to the remove_min : O(n^2)
* Conclusion
  1. AdaptablePriorityQueue : O(n^2 log(n))
     * why?
       * O( (n+m)*log(n) ) runs in O(n^2 log(n)) in worst case
  2. UnsortedPriorityQueue : O(n^2)
     * why?
       * Likewise, O( n^2 + m ) runs in O(n^2) in worst case

<br>

#### Analysis) Comparing the Two Implementations
* Key : the number of edges in a graph
  * When the number of edges in the graph is small [AdaptablePriorityQueue](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L191) is preferred.
  * When the number of edges in the graph is small [UnsortedPriorityQueue](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L265) is preferred.
* why?
  * Recall that the running time was
    * AdaptablePriorityQueue : O( (n+m)*log(n) )
    * UnsortedPriorityQueue : O(n^2)
  * Thus,
    * if m < (n^2)/log(n) : AdaptablePriorityQueue is better.
    * else : UnsortedPriorityQueue is better.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_06_03_dijkstra_implementation_prop.png" style="height : 150px;"></img><br/>
</p>


#### Tech.) Dijkstra's Algorithm with Fibonacci heap
* It runs in O(m + nlog(n)) time.

#### Tech.) Implementation : [Dijkstra’s Algorithm](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/shortest_paths.py#L5)
* Returns a map such that
  * key : vertex
  * value : distance from starting vertex to the key vertex

#### Tech.) Shortest-Path Tree
* Returns a map such that
  * key : vertex
  * value : incoming edge of the key vertex which is on the shortest path from the starting vertex


## 14.7 Minimum Spanning Trees
* Goal for the Minimum Spanning Tree
  * Computers connection example
    * Suppose we wish to connect all the computers in a new office building using **the least** amount of cable.
    * We can model this problem using an undirected, weighted graph G whose 
      * vertices represent the computers, and whose 
      * edges represent all the possible pairs (u,v) of computers
      * the weight w(u,v) of edge (u,v) is equal to the amount of cable needed to connect computer u to computer v
    * We are interested instead in finding a tree T that contains all the vertices of G and has the minimum total weight over all such trees.
      * Rather than computing a shortest-path tree from some particular vertex v

<br>

#### Def.) Problem Definition
* Given an undirected, weighted graph G, we are interested in finding a tree T that contains all the vertices in G and minimizes the sum
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_01_min_spanning_tree_def.png" style="height : 100px;"></img><br/>
</p>

* A tree, such as this, that contains every vertex of a connected graph G is said to be a **spanning tree**   
* The problem of computing a spanning tree T with smallest total weight is known as the **minimum spanning tree (or MST)** problem.
* In order to simplify the description of the algorithms, we assume, in the following, that the input graph G is undirected.

<br>

#### Concept) A Crucial Fact about Minimum Spanning Trees
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_02_min_spanning_tree_crucial_fact.png" style="width : 100%;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_03_min_spanning_tree_crucial_fact_image.png" style="height : 500px;"></img><br/>
</p>

### 14.7.1 Prim-Jarnik Algorithm
* Idea
  * Grow a minimum spanning tree from a single cluster starting from some “root” vertex s.
    * similar to the main idea of Dijkstra’s algorithm
* How?
  1. We begin with some vertex s, defining the initial “cloud” of vertices C.
  2. In each iteration, we choose a minimum-weight edge e = (u,v), connecting a vertex u in the cloud C to a vertex v outside of C.
     * Why it works?
       * Consider the [above crucial fact](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md#concept-a-crucial-fact-about-minimum-spanning-trees).
       * By always choosing the smallest-weight edge joining a vertex inside C to one outside C, we are assured of always adding a valid edge to the MST.
  3. The vertex v is then brought into the cloud C.
  4. Repeat the above process until a spanning tree is formed.

* Pseudo Code
```python
Algorithm PrimJarnik(G):
  Input: An undirected, weighted, connected graph G with n vertices and m edges
  Output: A minimum spanning tree T for G
  
  Pick any vertex s of G
  D[s] = 0
  for each vertex v != s do
    D[v] = ∞

  Initialize T = ∅.
  Initialize a priority queue Q with an entry (D[v],(v,None)) for each vertex v,
  where D[v] is the key in the priority queue, and (v,None) is the associated value.

  while Q is not empty do
    (u,e) = value returned by Q.remove min()
    Connect vertex u to T using edge e if e is not None (Consider the case of s)
    for each edge e` = (u,v) such that v is in Q do
      {check if edge (u,v) better connects v to T}
      if w(u,v) < D[v] then
        D[v] = w(u,v)
        Change the key of vertex v in Q to D[v].
        Change the value of vertex v in Q to (v,e`).
  return the tree T
```

#### Analysis) Performance of Prim-Jarnik Algorithm
* Similar to Dijkstra's Algorithm
  * Heap-based priority queue implementation : O( (m+n)*log(n) )
  * Unsorted priority queue implementation : O(n^2)

#### Tech.) Implementation : [Prim-Jarnik Algorithm](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/minimum_spanning_tree.py)

<br>

### 14.7.2 Kruskal’s Algorithm
* Idea
  * Recall that Prim-Jarn´ık algorithm builds the MST by growing a single tree until it spans the graph
  * On the other hand, Kruskal’s algorithm maintains a **forest** of clusters, repeatedly merging pairs of clusters until a single cluster spans the graph.
* How?
  1. Initially, each vertex is by itself in a singleton cluster
  2. The algorithm then considers each edge in turn, ordered by increasing weight.
  3. If an edge e connects two different clusters, then e is added to the set of edges of the minimum spanning tree.
     * Also, the two clusters connected by e are merged into a single cluster.
     * On the other hand, if e connects two vertices that are already in the same cluster, then e is discarded.
  4. Once the algorithm has added enough edges to form a spanning tree, it terminates and outputs this tree as the minimum spanning tree.

* Pseudo Code
```python
Algorithm Kruskal(G):
  Input: A simple connected weighted graph G with n vertices and m edges
  Output: A minimum spanning tree T for G
  
  for each vertex v in G do
    Define an elementary cluster C(v) = {v}.

  Initialize a priority_queue Q to contain all edges in G, using the weights as keys.
  T = ∅     {T will ultimately contain the edges of the MST}
  while T has fewer than n−1 edges do
    (u,v) = value returned by Q.remove min()
    Let C(u) be the cluster containing u, and let C(v) be the cluster containing v.
    if C(u) != C(v) then
      Add edge (u,v) to T.
      Merge C(u) and C(v) into one cluster.
  return tree T
```

#### Analysis) Performance of Kruskal’s Algorithm
* Conclusion : O(m log(n)) time.
* How?
  * Consider the following two points
    1. Ordering the edges
       * If the priority queue is Heap Priority Queue : O(m log(m)) time.
         * Considering the fact that m = n^2, O(m log(m)) = O(m log(n))
    2. Cluster Management
       * We must be able to find the clusters for vertices u and v that are endpoints of an edge e, to test whether those two clusters are distinct. 
         * If so, we should merge those two clusters into one.
       * Thus, we should consider the find operation and the union operation.
         * This will be covered as the next material : [disjoint partitions]()
         * There will be 2m find operations and n-1 union operations.
         * Simple union find structure can perform them in O(m+n log(n)) time.
  
#### Tech.) Implementation : [Kruskal’s Algorithm](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/GraphAlgorithms/minimum_spanning_tree.py#L41)

<br><br>

### 14.7.3 Disjoint Partitions and Union-Find Structures
* Target
  * a data structure for managing a partition of elements into a collection of disjoint sets.
  * an element belongs to one and only one of these sets
  * We do not expect to be able to iterate through the contents.
  * We will refer to the clusters of our partition as **groups**.
  * To differentiate between one group and another, we assume that at any point in time, each group has a designated entry that we refer to as the leader of the group.

<br>

#### Concept) Partition ADT
* Methods
  * make_group(x) : Create a singleton group containing new element x and return the position storing x.
  * union(p, q) : Merge the groups containing positions p and q.
  * find(p) : Return the position of the leader of the group containing position p.

<br>

#### Concept) Sequence Implementation
* The sequence for a group A stores element positions.
* Position object stores following variables
  1. element : references its associated element x and allows the execution of an element() method in O(1) time.
  2. group : references the sequence storing p, since this sequence is representing the group containing p’s element.
* Let first position in a sequence to serve as the leader.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_04_sequence_implementation_image.png" style="height : 400px;"></img><br/>
</p>

#### Prop.) When using the above sequence-based partition implementation, performing a series of k make group, union, and find operations on an initially empty partition involving at most n elements takes O(k+nlog(n)) time.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_05_partition_prop.png" style="width : 100%;"></img><br/>
</p>

<br>

#### Tech.) A Tree-Based Partition Implementation
* Concept
  * a collection of trees to store the n elements, where each tree is associated with a different group.
  * We implement each tree with a linked data structure whose nodes are themselves the group position objects.
  * Each position p as being a node having instance variables as follows
    1. element : refers to its element x
    2. parent : refers to its parent node
  * By convention, if p is the root of its tree, we set p’s parent reference to itself.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/images/14_07_06_tree_implementation_image.png" style="width : 100%;"></img><br/>
</p>






## 14.8 [Exercises](https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_08_exercises.md)