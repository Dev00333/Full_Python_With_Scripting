def sum_of_max_substring(arr):
    if not arr: return "Invalid array"
    s=ms=arr[0]
    for i in range(1,len(arr)):
        s=max(arr[i],s+arr[i])
        ms=max(ms,s)
    return ms