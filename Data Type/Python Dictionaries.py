thisdict = {
  "name": "Asif",
  "branch": "Computer",
  "roll": "20MH1A0504",
  "birth": 1999
}
print(thisdict)

#check length
print(len(thisdict))

#check type
print(type(thisdict))

thisdict = {
  "name": "Asif",
  "branch": "Computer",
  "roll": "20MH1A0504",
  "birth": 1999
}

x = thisdict.keys()

print(x) #before the change

thisdict["blood"] = "O+"

print(x) #after the change

#loop
for x, y in thisdict.items():
    print(x, y)