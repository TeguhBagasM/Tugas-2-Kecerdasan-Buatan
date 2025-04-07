def depth_limited_search(graph, start, goal, depth_limit):
    def recursive_dls(path, depth):
        node = path[-1]
        if node == goal:
            return path
        if depth == 0:
            return "cutoff"
        cutoff_occurred = False
        neighbors = graph.get(node, [])
        
        for neighbor, _ in neighbors:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                result = recursive_dls(new_path, depth - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != None:
                    return result
        return "cutoff" if cutoff_occurred else None
    return recursive_dls([start], depth_limit)
def iterative_deepening_dfs(graph, start, goal):
    depth = 0
    while True:
        result = depth_limited_search(graph, start, goal, depth)
        if result != "cutoff":
            return result
        depth += 1
graph = {
    'S': [('A', 3), ('C', 2)],
    'A': [('B', 1)],
    'B': [('G', 7), ('D', 3)],
    'C': [('D', 6), ('B', 5)],
    'D': [('G', 1)],
    'G': []
}
start_node = 'S'
goal_node = 'G'
id_dfs_path = iterative_deepening_dfs(graph, start_node, goal_node)
print("Iterative Deepening DFS Path:", " → ".join(id_dfs_path))