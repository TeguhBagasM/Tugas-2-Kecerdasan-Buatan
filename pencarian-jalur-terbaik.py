def uniform_cost_search(graph, start, goal):
    # Priority queue untuk menyimpan (biaya, jalur)
    priority_queue = [(0, [start])]
    visited = set()
    
    while priority_queue:
        priority_queue.sort()  # Sort berdasarkan biaya
        cost, path = priority_queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, edge_cost in graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = list(path)
                    new_path.append(neighbor)
                    priority_queue.append((new_cost, new_path))
    return None, float('inf')
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
optimal_path, optimal_cost = uniform_cost_search(graph, start_node, goal_node)

print("Jalur Optimal (Branch and Bound):", " → ".join(optimal_path))
print("Biaya Jalur Optimal:", optimal_cost)