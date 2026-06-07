# Find the longest word in a sentence that has all unique characters.


st = "Python programming is fun and useful for beginners"

l = st.split(" ")

unq = []

for i in l:
    if len(i) == len(set(i)):
        unq.append(i)
    
print(unq)