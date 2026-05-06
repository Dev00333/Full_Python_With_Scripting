def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    try:
        if(y==0):
            print()
    except Exception as e:
        print(e)
    else:
        return x/y
def mod(x, y):
    return x%y