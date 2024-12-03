import time

from sorting.quick_sort import quick_sort
from sorting.merge_sort import merge_sort
from sorting.selection_sort import selection_sort


if __name__ == "__main__":
    arr = [22, 1, 45, 77, 32, 21, 56]
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    weight_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
