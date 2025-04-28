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
                continue  # Branch and Bound: Skip if exceeding current best
            if is_valid(v, color, c):
                color[v] = c
                backtrack(v + 1, color, m, best_solution)
                color[v] = 0  # Backtrack

    min_colors = float('inf')
    best_solution = [0] * len(adj_matrix)
    color = [0] * len(adj_matrix)
    backtrack(0, color, m, best_solution)
    return best_solution if min_colors != float('inf') else None