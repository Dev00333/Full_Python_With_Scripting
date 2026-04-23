arr = [ 'a', 'b', 'c', 'd', 'e' ]
print(arr[0]) # a
print(len(arr)) # 5
print(arr[1:4]) # ['b', 'c', 'd']
courses = ['math', 'physics', 'chemistry']
test_course = ['biology', 'english']
courses.append('computer science')
print(courses) # ['math', 'physics', 'chemistry', 'computer science']
courses.extend(test_course)
print(courses) # ['math', 'physics', 'chemistry', 'computer science', 'biology', 'english']
courses.insert(2, 'history')
print(courses) # ['math', 'physics', 'history', 'chemistry', 'computer science', 'biology', 'english']
courses.remove('physics')
print(courses) # ['math', 'history', 'chemistry', 'computer science',
courses.pop()
print(courses) # ['math', 'history', 'chemistry', 'computer science', 'biology']
courses.pop(3)
print(courses) # ['math', 'history', 'chemistry', 'biology']
courses.reverse()  
print(courses) # ['biology', 'chemistry', 'history', 'math']
courses.sort()
print(courses) # ['biology', 'chemistry', 'history', 'math']
for item in courses:
    print(item) # biology, chemistry, history, math
for index, item in enumerate(courses):
    print(index, item) # 0 biology, 1 chemistry, 2 history, 3 math
    sorted_courses = sorted(courses)
print(sorted_courses) # ['biology', 'chemistry', 'history', 'math']
course_string = ', '.join(courses)
print(course_string) # biology, chemistry, history, math
courses2 = course_string.split(', ')
print(courses2) # ['biology', 'chemistry', 'history', 'math']   


# tuples are similar to lists but they are immutable, which means that we cannot change the values of a tuple after it has been created. We can create a tuple by using parentheses instead of square brackets.
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) # (1, 2, 3, 4, 5)
tuple1.__add__((6, 7, 8)) # (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1) # (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8)
tuple3 = tuple1 + tuple2
print(tuple3) # (1, 2, 3, 4, 5, 6, 7, 8)

# sets are unordered collections of unique elements. We can create a set by using curly braces or the set() function.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1) # {1, 2, 3, 4, 5}
print(set2) # {4, 5, 6, 7, 8   }
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # {4, 5}