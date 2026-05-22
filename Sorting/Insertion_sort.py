import random
# this is insertion sort algorithm
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

while True:
    try:
        x=int(input("Enter the length of the array you want to sort: "))
        a=[random.randint(1,100) for i in range (x)]
        print(f"the sorted array is: {insertion_sort(a)}")
        break
    except ValueError:
        print("Please enter a valid integer.")

# Practice:
#   def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#       key=arr[i]
#       j=i-1
#       while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#       arr[j+1]=key
#     return arr