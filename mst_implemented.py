import numpy as np
import scipy.sparse as sp
import scipy.io as sio

# Load a sparse matrix from the SuiteSparse Matrix Collection
mat = sio.mmread("/Users/jithinrajan/Downloads/1138_bus/1138_bus.mtx").tocsr()

# Convert the matrix into an adjacency list representation
adj_list = {}
for i in range(mat.shape[0]):
    adj_list[i] = []
    row_indices = mat.indptr[i:mat.indptr[i+1]]
    for j in row_indices:
        if j >= len(mat.data):
            print(f"Error: Index {j} is out of bounds for data array.")
            break
        if mat.data[j] != 0:
            adj_list[i].append((mat.indices[j], mat.data[j]))
            
# Implement Prim's algorithm on the adjacency list
def prim(adj_list):
    visited = set()
    queue = [(0, 0)]
    mst = []
    while queue:
        weight, u = queue.pop(0)
        if u is None or u in visited:
            continue
        visited.add(u)
        mst.append((u, weight))
        for v, w in adj_list[u]:
            if v not in visited:
                queue.append((w, v))
    return mst

# Test the implementation on the adjacency list
mst = prim(adj_list)
print(mst)
