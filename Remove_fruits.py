fruits = ["apple", "banana", "coconut", "srawberry", "kiwi"]
fruit = input("Which fruit would you like to remove?: ")
if fruit in fruits:
	fruits.remove(fruit)
print(fruits)