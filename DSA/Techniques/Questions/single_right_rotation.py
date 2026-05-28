def single_right_rotation(arr):
    l=len(arr)
    if l<2:
        return arr
    element=arr[l-1]
    for i in range(l-1):
        arr[l-1-i]=arr[l-2-i]
    arr[0]=element
    return arr

def slice_right_shift(arr):
    return arr[-1:]+arr[:-1] if arr else []

def slice_in_place(arr):
    arr[:]=arr[-1:]+arr[0:-2]
    return arr