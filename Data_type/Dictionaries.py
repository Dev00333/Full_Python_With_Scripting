student = {
        "John": {
        "age": 20,
        "grade": "A",
        "courses": ["math", "physics", "chemistry"]
    },
    "Jane": {
        "age": 22,
        "grade": "B",
        "courses": ["biology", "english"]
    }
}
print(student.keys()) # dict_keys(['John', 'Jane'])
print(student.values()) # dict_values([{'age': 20, 'grade': 'A', 'courses': ['math', 'physics', 'chemistry']}, {'age': 22, 'grade': 'B', 'courses': ['biology', 'english']}])
print(student["John"]) # {'age': 20, 'grade': 'A', 'courses': ['math', 'physics', 'chemistry']}
print(student["John"].get("age")) # 20
student["John"].update({"age": 21})
print(student["John"]) # {'age': 21, 'grade': 'A', 'courses': ['math', 'physics', 'chemistry']}
student["John"]["courses"].append("computer science")
student["John"].update({"phone": "1234567890"})
print(student["John"]) # {'age': 21, 'grade': 'A', 'courses': ['math', 'physics', 'chemistry', 'computer science'], 'phone': '1234567890'}
student["Jane"]["courses"].remove("english")
print(student["Jane"]) # {'age': 22, 'grade': 'B', 'courses': ['biology']}
student.pop("Jane")
print(student) # {'John': {'age': 21, 'grade': 'A', 'courses': ['math', 'physics', 'chemistry', 'computer science'], 'phone': '1234567890'}}
print(student.__len__()) # 1