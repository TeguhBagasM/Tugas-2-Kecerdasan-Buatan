from collections import deque

def bidirectional_search(graph, start, goal):
    # Buat graf dengan arah terbalik
    reverse_graph = {}
    for node in graph:
        for neighbor, cost in graph[node]:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append((node, cost))
    
    # Inisialisasi pencarian dari awal dan tujuan
    forward_queue = deque([[start]])
    backward_queue = deque([[goal]])
    
    forward_visited = {start: [start]}
    backward_visited = {goal: [goal]}
    
    while forward_queue and backward_queue:
        # Perluas pencarian maju
        path = forward_queue.popleft()
        node = path[-1]
        
        # Periksa tetangga dalam pencarian maju
        for neighbor, _ in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            
            if neighbor not in forward_visited:
                forward_queue.append(new_path)
                forward_visited[neighbor] = new_path
            
            if neighbor in backward_visited:
                backward_path = backward_visited[neighbor]
                combined_path = new_path + backward_path[1:][::-1]
                return combined_path
        
        # Perluas pencarian mundur
        path = backward_queue.popleft()
        node = path[-1]
        
        # Periksa tetangga dalam pencarian mundur
        for neighbor, _ in reverse_graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            
            if neighbor not in backward_visited:
                backward_queue.append(new_path)
                backward_visited[neighbor] = new_path
            
            if neighbor in forward_visited:
                forward_path = forward_visited[neighbor]
                combined_path = forward_path + new_path[1:][::-1]
                return combined_path
    
    return None

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
bi_path = bidirectional_search(graph, start_node, goal_node)

print("Bidirectional Search Path:", " → ".join(bi_path))