
import sys

sys.path.append("C:\\Users\\Devang Mishra\\OneDrive\\Desktop\\workspace\\python")
from sample import student as s
from sample import roll_number as r

print(sys.path)
def student_name(number):
    if 0 <= number < len(s):
        print(f"the student at index {number} is {s[number]}")
    else:
        print(f"index {number} is out of range")
def student_finder(name):
    for i in range(len(s)):
        if s[i].lower() == name.lower():
            return print(f"student {name} found in the list at index {i}")
    return print(f"student {name} not found in the list")
def student_at_roll_number(number):
    for i in range (len(r)):
        if r[i] == number:
            return print(f"student at roll number {number} is {s[i]}")

student_name(0)
student_finder("charlie")
student_at_roll_number(2)