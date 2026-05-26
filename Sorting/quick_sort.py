import random

def quick_sort_in_place(arr, low, high):
    pivot = arr[low]
    if low < high:
        i = low
        j = high
        while i < j:
            while arr[i] <= pivot and i < high:
                i += 1
            while arr[j] > pivot and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = quick_sort_in_place(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# here the time complexity is O(n log n) and space complexity is O(log n) on average, but in the worst case (when the smallest or largest element is always chosen as the pivot), it can degrade to O(n^2) time complexity.