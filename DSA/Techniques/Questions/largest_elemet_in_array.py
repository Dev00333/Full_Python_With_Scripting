import random
def largest_element(arr):
    if not arr:
        return None
    max_element = arr[0]
    for i in range(1, len(arr)):
        max_element = max(max_element, arr[i])
    return max_element
while True:
    try:
        user_in_format = input("manual(m) or random(r) input or quit(q): ")
        if user_in_format.lower() == 'm':
            try:
                size = int(input(f"Enter the size of array: "))
                arr = []
                while len(arr) < size:
                    element = int(input(f"Enter element {len(arr) + 1}: "))
                    arr.append(element)
                print(f"Array: {arr}")
                print(f"Largest element in the array: {largest_element(arr)}")
                break
            except ValueError:
                print("Please enter valid integers for size and array elements.")
        elif user_in_format.lower() == 'r':
            while True:
                try:
                    size =  int(input(f"Enter the size of array:"))
                    range_limit_begin = 0
                    range_limit_end = 100
                    while True:
                        custom = input("Do you want to set a custom range for random numbers? (y/n):")
                        if custom.lower() == 'n':
                            break
                        elif custom.lower() == 'y':
                            while True:
                                range_limit_begin = int(input(f"Enter begining of the range limit for random numbers:"))
                                range_limit_end = int(input(f"Enter the end of range limit of random numbers:"))
                                if range_limit_begin < range_limit_end:
                                    break
                                else:
                                    print("Please enter a valid range where the beginning is less than the end.")
                            break
                        else:
                            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                    arr = [random.randint(range_limit_begin, range_limit_end) for _ in range(size)]
                    print(f"Array: {arr}")
                    print(f"Largest element in the array: {largest_element(arr)}")
                    break
                except ValueError:
                    print("Please enter valid integers for size and range limit.")
            break
        elif user_in_format.lower() == 'q':
            print("Quitting the program.")
            break
        else:
            print("Invalid input format. Please enter 'm' for manual or 'r' for random input.")
    except KeyboardInterrupt:
            print("\nQuitting the program.")
            break