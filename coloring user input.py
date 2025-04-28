v = int(input("Enter the number of vertices: "))  # Number of vertices in the graph

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

# Input for the graph adjacency matrix
graph = []
print("Enter the adjacency matrix row by row:")
for i in range(v):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    graph.append(row)

# Input for the number of colors
m = int(input("Enter the number of colors: "))

color = [0] * v  # Array to store colors for each vertex

# Start the backtracking process
if not main(graph, m, 0, color):
    print("No valid coloring found.")
