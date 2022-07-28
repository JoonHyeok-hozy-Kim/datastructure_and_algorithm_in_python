

from copy import deepcopy
def floyd_warshall(g):
    closure = deepcopy(g)
    vertices = list(closure.vertices())
    n = len(vertices)
    for k in range(n):
        # Get i-th vertex that is connected to k-th
        for i in range(n):
            if i != k and closure.get_edge(vertices[i], vertices[k]) is not None:
                # Get j-th vertex that is connected to k-th
                for j in range(n):
                    if j != k and closure.get_edge(vertices[j], vertices[k]) is not None:

                        # Check if i-th and j-th are not connected yet
                        if closure.get_edge(vertices[i], vertices[j]) is None:
                            closure.insert_edge(vertices[i], vertices[j])   # Add new edge!
    return closure