st1 = "I love Python and data science"
st2 = "Python is useful for data analysis"

st1 = set(st1.split(" "))
st2 = set(st2.split(" "))

print(st1.intersection(st2))