student = {"name":"Amit", "age":20}

student.setdefault("class", "Btech")
print(student)

student.update({"class":"BCA"})
print(student)

student.pop("age")
print(student)

poped = student.popitem()
print(student)
print(poped)


student1 = {"name":"Amit"}

# Q1: "age" ko setdefault se 18 add karo
student1.setdefault("age", 18)
print("\n\n", student1)
# Q2: "name" ko setdefault se try karo (kya output aayega?)
student1.setdefault("name", "Anshul")
print(student1)