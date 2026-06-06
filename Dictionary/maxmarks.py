marks = {
    "Amit": 50,
    "Rahul": 80,
    "Neha": 70,
    "Suresh": 65
}

max = -1
Sname = ""

for name, marks in marks.items():
    if max < marks:
        max = marks
        Sname = name

print(Sname)