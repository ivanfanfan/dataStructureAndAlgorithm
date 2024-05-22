"""
Represented as a collection of linked lists.
There is an array of pointer which points to the edges connected to
that vertex
"""

def create_adjacency_list(edges, num_vertices):
    # Initialize the adjacency list
    adj_list = [[] for _ in range(num_vertices)]

    # Fill the adjacency list based on the edges in the graph
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list
# list.append  add an object to the end of the list.



if __name__ == '__main__':
    # undirected graph of 4 nodes
    num_vertices = 4
    edges = [(0,1),(0,2),(1,2),(2,3),(3,1)]

    adj_list = create_adjacency_list(edges, num_vertices)

    for i in range(num_vertices):
        print(f"{i} -> {' '.join(map(str,adj_list[i]))}")