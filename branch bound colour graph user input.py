def graph_coloring(adj_matrix, m):
    def is_valid(v, color, c):
        for i in range(len(adj_matrix)):
            if adj_matrix[v][i] and color[i] == c:
                return False
        return True

    def backtrack(v, color, m, best_solution):
        nonlocal min_colors
        if v == len(adj_matrix):
            used_colors = max(color)
            if used_colors < min_colors:
                min_colors = used_colors
                best_solution[:] = color.copy()
            return

        for c in range(1, m + 1):
            if c >= min_colors:
                continue  # Prune if worse than current best
            if is_valid(v, color, c):
                color[v] = c
                backtrack(v + 1, color, m, best_solution)
                color[v] = 0  # Backtrack

    min_colors = float('inf')
    best_solution = [0] * len(adj_matrix)
    color = [0] * len(adj_matrix)
    backtrack(0, color, m, best_solution)
    return best_solution if min_colors != float('inf') else None

def main_graph_coloring():
    print("Graph Coloring Solver (Branch and Bound)")
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (row-wise, 0/1):")
    adj_matrix = []
    for _ in range(n):
        while True:
            row = input().strip().split()
            if len(row) == n:
                try:
                    adj_matrix.append([int(x) for x in row])
                    break
                except ValueError:
                    print("Please enter 0 or 1 only!")
            else:
                print(f"Please enter exactly {n} values per row!")
    m = int(input("Enter maximum colors allowed: "))
    coloring = graph_coloring(adj_matrix, m)
    if coloring:
        print("\nOptimal Coloring:")
        print("Vertex\tColor")
        for v, c in enumerate(coloring, 1):
            print(f"{v}\t{c}")
    else:
        print("No valid coloring exists!")

if __name__ == "__main__":
    main_graph_coloring()