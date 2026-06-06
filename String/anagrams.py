s1 = str(input("Enter the First String : "))
s2 = str(input("Enter the Second String : "))

s1 = sorted(s1)
s2 = sorted(s2)

if s1 == s2:
    print("anagrams")
else:
    print("Not anagrams")


# Word 1	Word 2	Anagram?
# care  	race	✅
# heart	    earth	✅
# hello	    world	❌