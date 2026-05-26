def check_sorted(arr):
    l=len(arr)
    if l<=1:
        return True
    ascending = arr[-1] >= arr[0]
    for i in range(1, l):
        if (ascending and arr[i] < arr[i - 1]) or (not ascending and arr[i] > arr[i - 1]):
            return False
    return True