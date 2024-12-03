def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    # Рекурсивно посещаем всех соседей
    for neighbor in graph[start]:
        if neighbor not in visited:
            print(neighbor, end=" ")    
            dfs(graph, neighbor, visited)
    
    return visited