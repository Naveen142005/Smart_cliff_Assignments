# 29. Longest Consecutive Sequence

# Reading input
n = int(input())
arr = list(set(map(int, input().split())))

                        # UNION FIND ALGORITHM

# DSU parent array
parent = [i for i in range(n)]

# tracking size of each set
size = [1] * n

# mapping value to the index
indexes = dict()
for i in range(n):
    indexes[arr[i]] = i

# path compression
def find_ultimate_parent(p):
    if parent[p] == p:
        return p
    parent[p] = find_ultimate_parent(parent[p])
    return parent[p]

# union by size
def union_find(u, v):
    u = find_ultimate_parent(u)
    v = find_ultimate_parent(v)
    if u == v:
        return
    if size[u] < size[v]:
        parent[u] = v
        size[v] += size[u]
    else:
        parent[v] = u
        size[u] += size[v]

# union consecutive numbers
for i in range(n):
    if arr[i] + 1 in indexes:
        union_find(i, indexes.get(arr[i] + 1))
    if arr[i] - 1 in indexes:
        union_find(i, indexes.get(arr[i] - 1))

# Result
print(max(size) if size else 0)
