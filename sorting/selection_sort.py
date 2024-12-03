import typing


def selection_sort(source: typing.List[int]) -> typing.List[int]:
    """
    Sort the source array using selection sorting algorithm with O(n^2) complexity.
    Return a new sorted array.
    """
    _arr = source.copy() # Create a temporary array from source
    n = len(_arr)

    for i in range(n):
        min_index = i # Assume min index of unsorted part of the array
        for j in range(i + 1, n):
            if _arr[j] < _arr[min_index]:
                min_index = j
        
        if min_index != i:
            current_min = _arr[i]
            _arr[i] = _arr[min_index]
            _arr[min_index] = current_min

    return _arr
