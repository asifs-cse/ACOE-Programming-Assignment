welcom = "Welcome to Python programming. "
name = str(input("Enter your naem: "))
print(f"Hello {name}", welcom)

#slicing
print(f"slicing with range: {name[0:5]}")
#Slice From the Start
print(f"slicing from start: {name[:5]}")
#Slice To the End
print(f"slicing to end: {name[2:]}")
#Negative Indexing
print(f"slicing to end: {name[-5:-2]}")
#Upper Case
print(name.upper())
#Lower Case
print(name.lower())
#split string
print(name.split(","))
#Replace String
print(name.replace("a","A"))
#Remove Whitespace
print(name.strip())
#String formatting
name_ex = "Your name is {}"
print(name_ex.format(name))
#Escape Characters
print(f"Hello \"{name}\"")