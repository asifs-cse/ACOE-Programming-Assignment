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