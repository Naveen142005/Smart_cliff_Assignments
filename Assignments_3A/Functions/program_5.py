# 5. Longest Consecutive Sequence

            # UNION FIND ALGORITHM

def find_ultimate_parent(p, parent):
    if parent[p] == p:
        return p
    parent[p] = find_ultimate_parent(parent[p], parent)  # Path compression
    return parent[p]

def union_find(u, v, parent, size):
    u = find_ultimate_parent(u, parent)
    v = find_ultimate_parent(v, parent)
    if u == v:
        return
    if size[u] < size[v]:
        parent[u] = v
        size[v] += size[u]
    else:
        parent[v] = u
        size[u] += size[v]

def longest_consecutive_sequence(arr):
    n = len(arr)
    parent = [i for i in range(n)]
    size = [1] * n
    indexes = {arr[i]: i for i in range(n)}

    # union consecutive numbers
    for i in range(n):
        if arr[i] + 1 in indexes:
            union_find(i, indexes[arr[i] + 1], parent, size)
        if arr[i] - 1 in indexes:
            union_find(i, indexes[arr[i] - 1], parent, size)

    return max(size) if size else 0

def main():
    # Reading input
    n = int(input())
    arr = list(set(map(int, input().split())))  # remove duplicates
    print(longest_consecutive_sequence(arr))

if __name__ == "__main__":
    main()
