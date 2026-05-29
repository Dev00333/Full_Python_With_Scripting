def search_linear(arr, element):
    l=len(arr)
    for i in range(l):
        if arr[i]==element: return True
    return False

def search_linear_two_pointer(arr,element):
    l=len(arr)
    i=0
    j=l-1
    while(i<=j):
        if arr[i]==element or arr[j]==element: return True
        else:
            i+=1
            j-=1
    return False