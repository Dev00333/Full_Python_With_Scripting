import random
# this is selection sort algorithm

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
while True:
    try:
        x=int(input("Enter the length of the array you want to sort: "))
        a=[random.randint(1,100) for i in range (x)]
        print(f"the sorted array is: {selection_sort(a)}")
        break
    except ValueError:
        print("Please enter a valid integer.")
