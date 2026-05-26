def remove_duplicates(arr):
    if not arr:
        return []
    unique = arr[0]
    count = 1
    l=len(arr)
    for i in range(1, l):
        if arr[i] != unique:
            unique = arr[i]
            count += 1
            arr[count -1] = unique
    return arr