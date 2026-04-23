# and
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive.")
# or
a = 3
b = 7
if a > 0 or b > 0:
    print("At least one of a or b is positive.")
# not
c = -2
if not c > 0:
    print("c is not positive.")

# none 
d = None
if d is None:
    print("d is None.")
else:
    print("d is not None.")

# an empty sequence is considered False
my_list = []  # or an empty string, empty tuple, etc.
if not my_list:
    print("The list is empty.")

# any empty mapping is also considered False
my_dict = {}
if not my_dict:
    print("The dictionary is empty.")

# there are also some special values that are considered False, such as 0, 0.0, and False itself and aslo some user-defined classes can define their own __bool__ method to determine their truthiness.