# the try catch block in general catches the errors and gives out the suitable outut that we require
# in try block we write the  code we think will cause the problem and the expect block catches the error and returns the output we requested

try:
    f = open('test_file.txt')
except:
    print("the file doesnt exist") # this is a very general try catch and it will catch all errors in a sinh=gle statement

try:
    a = open('text.txt')
except FileNotFoundError:
    print("no file present named text.txt") # this is not a general error handeling in this we provide what error tio expect and can chain multiple except to catch each error
except Exception:
    print("sorry , some error occured")  # we have to make sure that the exceptions are given in a order particular errors first then as we go down we add general exception
else:           # this blockk of code only runs if no error is found in the try block
    print(a.read())
    a.close()
finally:
    print("successfully ran the script")