from heapq import heappop, heappush

def prim_algorithm(graph):

    # Choose the first vertex as the starting point
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])

    # Initialize the heap with edges connected to the starting vertex
    heap = [(cost, start_vertex, to_vertex) for to_vertex, cost in graph[start_vertex].items()]

    # Initialize the MST and the total weight
    mst = []
    total_weight = 0

    # Loop until we have processed all vertices
    while heap:
        cost, from_vertex, to_vertex = heappop(heap)
        if to_vertex in visited:
            continue
        mst.append((from_vertex, to_vertex, cost))
        total_weight += cost
        visited.add(to_vertex)
        for to_vertex, cost in graph[to_vertex].items():
            if to_vertex not in visited:
                heappush(heap, (cost, from_vertex, to_vertex))

    return mst, total_weight
