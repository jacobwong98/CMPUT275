'''
Exercise 3: Bellman Ford and Graph Potentials
Name: Jacob Wong


SOURCES:
Bellman Ford Algorithm
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
'''


def bellman_ford(vertices, edges, start):
    '''
    Computes shortest paths to every reachable vertex from the vertex "start"
    in the given directed graph.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
    example - {('A', 'B'): -3} means the edge from vertex
    'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    Assumes the graph does not have negative cost cycles,
    that all edges have endpoints in "vertices", and that
    "start" is also in "vertices".

    returns dist, reached

    Here reached is the search tree to all reachable vertices along
    minimum-cost paths and dist[v] is the cost to v along
    this path. If v is not reachable, it should not be in the
    search tree nor an index in dist.

    >>> vertices = {1, 2, 3, 4, 5, 6}
    >>> edges = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
    >>> dist, reached = bellman_ford(vertices, edges, 1)
    >>> print(dist)
    {1: 0, 2: 5, 3: 4, 4: 2, 5: -2}
    >>> print(reached)
    {1: 1, 2: 1, 3: 5, 4: 5, 5: 2}

    >>> vertices = {1, 2, 3, 4}
    >>> edges = {(1,2):3, (2,3):-2, (3,2):-3, (2,4):4}
    >>> dist, reached = bellman_ford(vertices, edges, 1)
    >>> print(dist)
    {1: 0, 2: -7, 3: -9, 4: -3}
    >>> print(reached)
    {1: 1, 2: 3, 3: 2, 4: 2}

    >>> vertices = {0, 13, 9, 24}
    >>> edges = {(0,13):5, (13,9):3, (9,24):2, (0, 24):4, (24, 13):-6}
    >>> dist, reached = bellman_ford(vertices, edges, 0)
    >>> print(dist)
    {24: 2, 9: 0, 13: -4, 0: 0}
    >>> print(reached)
    {0: 0, 24: 9, 13: 24, 9: 13}
    '''
    distance = {}
    reached = {start: start}

    for vertice in vertices:
        if vertice != start:
            distance[vertice] = float('inf')
        else:
            distance[vertice] = 0

    for vertice in range(len(vertices) - 1):
        for edge in edges.keys():
            if distance[edge[0]] + edges[edge] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + edges[edge]
                reached[edge[1]] = edge[0]
    for vertice in vertices:
        if distance[vertice] == float('inf'):
            del distance[vertice]
    return distance, reached


def find_potential(vertices, edges):
    '''
    Finds a potential for the graph or determines the graph has
    a negative-cost cycle.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
    example - {('A', 'B'): -3} Uploading, please wait... means the edge from vertex
    'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    If the graph has a negative-cost cycle, this simply returns None.
    Otherwise, it returns a dictionary mapping each vertex to its value
    in a potential function.

    >>> vertices = {1, 2, 3, 4, 5, 6}
    >>> edges = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
    >>> print(find_potential(vertices, edges))
    {1: 8, 2: 3, 3: 4, 4: 6, 5: 10, 6: 0}
    >>> edges[(5,4)] = 3   # creates a negative-cost cycle
    >>> print(find_potential(vertices, edges))
    None

    >>> vertices = {1, 2, 3, 4}
    >>> edges = {(1,2):3, (2,3):4, (3,2):-3, (2,4):4}
    >>> print(find_potential(vertices, edges))
    {1: 0, 2: 3, 3: 0, 4: 0}
    >>> edges[(2,3)] = -2
    >>> find_potential(vertices, edges) == None
    True

    >>> vertices = {0, 13, 9, 24}
    >>> edges = {(0,13):5, (13,9):3, (9,24):2, (0, 24):4, (24, 13):6}
    >>> print(find_potential(vertices, edges))
    {24: 0, 9: 0, 13: 0, 0: 0}
    >>> edges[(24,13)] = -6
    >>> find_potential(vertices, edges) == None
    True
    '''
    distance = {}

    for vertice in vertices:
        distance[vertice] = 0

    for vertice in range(len(vertices) - 1):
        for edge in edges.keys():
            if distance[edge[0]] + edges[edge] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + edges[edge]

    for vertice in vertices:
        cost, reached = bellman_ford(vertices, edges, vertice)
        if cost[vertice] < 0:
            return
        distance[vertice] = -distance[vertice]

    return distance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
