

def create_adjacency_list(edges, num_vertices):
    adjacency_list = [[] for _ in range(num_vertices)]

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list

if __name__ == '__main__':

    num_vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]

    adjacency_list = create_adjacency_list(edges, num_vertices)

    for i in range(num_vertices):
        print(f"{i} -> {' '.join(map(str, adjacency_list[i]))}")