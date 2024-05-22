"""
    representation of graph
        adjacency matrix
        adjacency list
"""
def create_adjacency_matrix(graph):
    # get the number of vertices in the graph

    num_vertices = len(graph)

    #initialize the adjacency matrix with zeros
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # fill the adjacency matrix based on the edges in the graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                # For undirected graph, set symmetric entries
                adj_matrix[j][i] = 1
    return adj_matrix

graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
adj_matrix = create_adjacency_matrix(graph)

# print the adjacency matrix
for row in adj_matrix:
    print(' '.join(map(str,row)))
    # TODO map(str,row)

