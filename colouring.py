v = 4  # Number of vertices in the graph

# Function to check if the coloring is valid
def check_color(graph, color):
    for i in range(v):
        for j in range(i + 1, v):
            if graph[i][j] == 1 and color[i] == color[j]:
                return False
    return True

# Function to print the colors of each vertex
def print_color(color):
    print("Following colors are:")
    for i in range(len(color)):
        print(f"Vertex {i + 1} = Color {color[i]}")

# Backtracking function to assign colors to the vertices
def main(graph, m, i, color):
    # If all vertices are processed, check if the coloring is valid
    if i == v:
        if check_color(graph, color):
            print_color(color)
            return True
        return False
    
    # Try different colors for the current vertex
    for u in range(1, m + 1):
        color[i] = u
        # Recursively color the next vertex
        if main(graph, m, i + 1, color):
            return True
        # Backtrack and reset the color
        color[i] = 0
    
    return False

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

m = 3  # Number of colors available
color = [0] * v  # Array to store colors for each vertex

# Start the backtracking process
main(graph, m, 0, color)
