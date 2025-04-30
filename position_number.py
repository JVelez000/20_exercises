numbers = [4, 8, 15, 16, 23, 42]
print("The list of numbers is: ", numbers)
n = int(input("Enter a number to search: "))
if n in numbers:
	print(f"Found at position {numbers.index(n) + 1}")
else:
	print("The number is not on the list. ")