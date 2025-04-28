# Original BFS code with user input
graph = {}
nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors = input(f"Enter neighbors for node {node} (space separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")

# BFS Implementation
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("\nFollowing is the Breadth-First Search")
bfs(visited, graph, start_node)
print("\n")

# DFS Implementation
visited_dfs = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited_dfs, graph, start_node)