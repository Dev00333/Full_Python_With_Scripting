import random
def merge_sort(arr):
    n=len(arr)
    if n<2:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # Append any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result

while True:
    try:
        a=int(input("Enter the number of elements in the array: "))
        arr = [random.randint(0,100) for i in range(a)]
        print(f"Original array: {arr}")
        sorted_arr = merge_sort(arr)
        print(f"Sorted array: {sorted_arr}")
        break
    except ValueError:
        print("Please enter a valid integer for the number of elements.")