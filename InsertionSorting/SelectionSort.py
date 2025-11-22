"""
Consider sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in A[1]. Then find the second smallest
element of A, and exchange it with A[2]. Continue in this manner for the first n-1
elements of A. Write this algorithm in python, which is known as selection
sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n - 1 elements, rather than for all n elements? Give the best-case
and worst-case running times of selection sort in theta -notation.
"""

def selection_sort(arr):
    n = len(arr)                
    for i in range(n - 1):
        min_value = i

        for j in range(i+1, n):
            if arr[j]< arr[min_value]:
                min_value = j
        
        arr[i], arr[min_value] = arr[min_value], arr[i]

    return arr


print(selection_sort([7,2,6,3,4,1]))





