from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbors = graph.get(node, [])
            
            for neighbor, _ in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
            
            visited.add(node)
    
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

# Jalankan BFS
start_node = 'S'
goal_node = 'G'
bfs_path = bfs(graph, start_node, goal_node)

print("BFS Path:", " → ".join(bfs_path))