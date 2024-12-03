import random
import typing

from utils.decorators import count_calls


@count_calls
def quick_sort(arr: typing.List[int]) -> typing.List[int]:
    """
    Sort the array using the quicksort algorithm.
    """
    if len(arr) <= 1: # <= Base case
        return arr
    
    piv_id = random.randint(0, len(arr) - 1)
    pivot = arr[piv_id] # <= Array split point
    lt_pivot = [] # <= Container for elements lower than pivot element
    gt_pivot = [] # <= Container for elements greater than pivot element

    for i in range(len(arr)):
        if i == piv_id:
            continue

        lt_pivot.append(arr[i]) if arr[i] < pivot else gt_pivot.append(arr[i]) 
    
    output = quick_sort(lt_pivot) + [pivot] + quick_sort(gt_pivot) # Order of output is important
    
    return output
