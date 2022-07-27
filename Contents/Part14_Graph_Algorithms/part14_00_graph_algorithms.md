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
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_dfs.py">DFS</a>

#### Concept) The existences of the dictionary, **discovered**, as an input parameter for DFS
* Purpose
  1. Internally, the dictionary provides a mechanism for recognizing visited vertices, as they will appear as keys in the dictionary.
  2. Externally, the DFS function augments this dictionary as it proceeds, and thus the values within the dictionary are the DFS tree edges at the conclusion of the process.
* Drawback
  * The dictionary data type that we used may run in **expected** O(1) time for a search, discovered[v] = e
    * Rather than the worst-case time.
    * It can be a violation to the property that we defined before. (Check the <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_00_graph_algorithms.md#analysis-running-time-of-depth-first-search">Assumption</a>)


#### Tech.) Reconstructing a Path from u to v
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_dfs.py#L17">construct_path(u, v, discovered)</a>
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
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_dfs.py#L17">is_connected?</a>


#### Tech.) Testing the Strong Connectivity of a Directed Graph
* How?
  * Choose an arbitrary vertex as a start.
  * Operate DFS search.
    * If there exists a vertex that is not visited, this graph is not strongly connected.
  * Now we have to check whether s is reachable from all other vertices.
    * With the DFS method, loop through all incoming edges to the current vertex.
      * This will run in O(m+n) time.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_dfs.py#L38">is_connected for indirect graph</a>


#### Tech.) Computing all Connected Components
* Target
  * For a not connected graph, we will identify 
    * all of the connected components of an undirected graph
    * the strongly connected components of a directed graph.
* How?
  * If an initial call to DFS fails to reach all vertices of a graph, we can restart a new call to DFS at one of those unvisited vertices.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_dfs.py#L65">DFS_complete</a>
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

#### Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/graph_bfs.py">BFS</a>

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




## 14.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part14_Graph_Algorithms/part14_08_exercises.md">Exercises</a>
