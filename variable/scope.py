#   LEGB
#   local enclosing global build-in
#   these values are the order of presedence the python checks the code
import sys
import builtins
x = 'global x'

def test():
    global x    # this explicitly tells the code to use the global variable x this variable global x will still work outside this def even after we comment out the real global x
    x = 'local x'   # this x is only local function so accessible inside the def function
    y = 'local y'
    print(x)    # as the x is the global variable so no error
test()
# print(y)    # the scope of y is inside the def function only so this throws and error
print(x)

def test1(z):
    print(z)
test1('local z')    # this is the enclosing variable

m = min([65464,684,987848,321546789])
print(m)

print(sys.builtin_module_names)
print(dir(builtins))