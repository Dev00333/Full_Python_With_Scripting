# in python their are inbuild functions for sortinhg the list, tuples or objects
# the sorting can also be done using user defined code and meathods
# the sorting of the list, tuple, object is generally done using the inbuild functions
#               - sorted: this creates new memory and stores the output or sortig n the new memory
#               - sort: this does not creates any new memory object and modifies the pre-existing data only
# we can also use the reverse order of sorting using the flag reverse=true in the meathod

a = [65,78,61,947,321,479,621,487,98]
a1 = sorted(a)                                                              # SPACE COMPLEXITY HERE IS O(N)
print(f"New list sorted: {a1} new memory is used")
a2 = sorted(a1, reverse = True)                                             # SPACE COMPLEXITY HERE IS O(N)
print(f"New list Reversed: {a2} new memory is used here also no recycling")
print(f"Orignal list: {a}")
a.sort()                                                                    # SPACE COMPLEXITY HERE IS O(1)~O(log N)
print(f"Sorted list: {a} list modification no new memory used")

di = {"name":"dev", "age":24, "gender":"male"}                              # dictonaries can also be sorted using the sorted meathod
s_di = sorted(di)
print(s_di)

l1 = [-648,-79,-64, 6646, 894751, -531894]
l1_as = sorted(l1)
print(f"Sorting when using the negative values: {l1_as}")
l1_abs = sorted(l1, key=abs)                                                 # in this sorting we sort using a key this help us set the parameters we want to sort ignoring the sign or other parameters
print(l1_abs)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.salary}"
    
e1 = Employee('dev', 22, 1000000)
e2 = Employee('shiv', 55, 455555)
e3 = Employee('akar', 28, 5000000)
employees = [e1, e2, e3]

valid_values = ["name", "age", "salary"]
para=input("enter the parameter you want to sort according to (name, age, salary): ")
while para not in valid_values:
    para=input("enter the valid parameter you want to sort according to (name, age, salary): ")
def e_sort(emp):
    return getattr(emp, para)                           # this inbuild attribute (getattr) we added makes sure that we get only the attribute we requested from the user rather than error
s_employee = sorted(employees, key=e_sort)
print(s_employee)
s1_employee_reversed = sorted(employees, key=e_sort, reverse=True)
print(s1_employee_reversed)

# we can also implement the above using the lambda function
# s_employee = sorted(employees, key=lambda emp: getattr(emp, para)) \n print(s_employee)
# s1_employee_reversed = sorted(employee, key=lambda emp: getattr(emp, para), reverse= True) \n print(s1_employee_reversed)