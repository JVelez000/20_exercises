names = ["Anna", "Luis", "Anna", "Carlos", "Anna", "robinson", "Luis", "Anna", "Carlos", "Anna", "robinson"]
print("List of names:", names)
name = input("Enter a name to count how many times it appears: ")
if name in names:
  print(f"{name} appears {names.count(name)} times")
else:
  print(f"{name} this name is not on the list")