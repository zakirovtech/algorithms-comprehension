import heapq


def dijkstra(graph, start):
    # Множество всех вершин
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    # Приоритетная очередь для выборки вершины с минимальным расстоянием
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Обрабатываем все соседи текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден кратчайший путь
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


# Пример графа с весами рёбер
weight_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_paths = dijkstra(weight_graph, 'A')
print("Shortest paths from 'A':", shortest_paths)
