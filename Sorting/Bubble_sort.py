import random

# this is bubble sort algorithm
def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        swapped=False
        for j in range (0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

while True:
    try:
        x=int(input("Enter the length of the array you want to sort: "))
        a=[random.randint(1,100) for i in range (x)]
        print(f"the sorted array is: {bubble_sort(a)}")
        break
    except ValueError:
        print("Please enter a valid integer.")