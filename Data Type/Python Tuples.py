thistuple = ("asif", "tamzid", "shamsul", "raza", "mamun")
print(thistuple)

# loop in touple
for x in thistuple:
  print(x)
  
#Range of Indexes
print(thistuple[2:5])

#Range of Negative Indexes
print(thistuple[-4:-1])

#condition in touples
thistuple = ("asif", "tamzid", "shamsul")
if "asif" in thistuple:
  print("Yes, 'asif' is in the fruits tuple")

#Multiply Tuples
fruits = ("asif", "tamzid", "shamsul")
mytuple = fruits * 2

print(mytuple)

thistuple = ("asif",)
print(type(thistuple))

#NOT a tuple
thistuple = ("asif")
print(type(thistuple))