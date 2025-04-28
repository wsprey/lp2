class Graph:
    def __init__(self, adjacency_list): 
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v): 
        return self.adjacency_list.get(v, [])

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H.get(n, 0)

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set()
        g = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            n = None
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


# User input for graph
adjacency_list = {}
nodes = input("Enter nodes separated by space (e.g., A B C D): ").split()

for node in nodes:
    neighbors = []
    neighbor_input = input(f"Enter neighbors for node {node} (format as 'B,1 C,3' for neighbors with weights): ").split()
    for item in neighbor_input:
        neighbor, weight = item.split(',')
        neighbors.append((neighbor, int(weight)))
    adjacency_list[node] = neighbors

# Create graph
graph = Graph(adjacency_list)

# User input for start and goal nodes
start_node = input("Enter start node: ")
stop_node = input("Enter stop node: ")

# Run A* algorithm
graph.a_star_algorithm(start_node, stop_node)