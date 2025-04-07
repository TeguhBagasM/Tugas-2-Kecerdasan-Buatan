def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in visited:
            if node == goal:
                return path
            
            visited.add(node)
            
            neighbors = graph.get(node, [])
            
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
    
    return None

# Definisi graf
graph = {
    'S': [('A', 3), ('C', 2)],
    'A': [('B', 1)],
    'B': [('G', 7), ('D', 3)],
    'C': [('D', 6), ('B', 5)],
    'D': [('G', 1)],
    'G': []
}

# Jalankan DFS
start_node = 'S'
goal_node = 'G'
dfs_path = dfs(graph, start_node, goal_node)

print("DFS Path:", " → ".join(dfs_path))