



if __name__ == '__main__':
    pass

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
