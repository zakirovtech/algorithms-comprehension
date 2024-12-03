import heapq

# У нас есть несортированный список
arr = [5, 1, 9, 3, 7, 6, 4]

# Преобразуем его в кучу
heapq.heapify(arr)

# Теперь извлекаем минимальные элементы
min_elem = heapq.heappop(arr)  # O(log n)
print(min_elem)  # 1

# Извлекаем следующий минимальный элемент
min_elem = heapq.heappop(arr)  # O(log n)
print(min_elem)  # 3