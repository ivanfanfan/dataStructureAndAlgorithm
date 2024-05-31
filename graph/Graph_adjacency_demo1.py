

def create_adjacency_matrix(graph):
    num_vertices = len(graph)

    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1

    return adj_matrix

graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

adj_matrix = create_adjacency_matrix(graph)

for row in adj_matrix:
    print(' '.join(map(str, row)))


