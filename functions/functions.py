def my_function():
    pass
# in this block we can simply pass other code to the function and it will not do anything, it will just pass the code and move on to the next line of code. This is useful when we want to create a function that we will implement later, or when we want to create a function that we will use as a placeholder for another function.

def my_function_with_args(a, b):
    c = a + b
    return c
# in this block we have created a function that takes two arguments, a and b, and returns the sum of a and b. We can call this function with different values for a and b to get different results. For example, if we call my_function_with_args(2, 3), it will return 5. If we call my_function_with_args(10, 20), it will return 30.

# we can also give nested functions, which are functions defined inside other functions. This can be useful for creating helper functions that are only used within the outer function.
def format_name(first_name, last_name):
    return "hello "+ f"{first_name} {last_name}"
print(format_name("john", "doe"))
# in this block we have created a function called format_name that takes two arguments, first_name and last_name, and returns a formatted string that says "hello" followed by the first name and last name. We can call this function with different values for first_name and last_name to get different results. For example, if we call format_name("john", "doe"), it will return "hello john doe". If we call format_name("jane", "smith"), it will return "hello jane smith".

def multi_input(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
students = ["john", "doe", "jane"]
info = {"age": 25, "city": "new york"}
multi_input(*students, **info)


# in the above example the *args unpacks the list of students and pass it individually to the def and **kwargs unpacks the dictionary of info and pass it as keyword arguments to the def. The output will be: