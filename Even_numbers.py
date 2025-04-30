# The underscore (_) is used here because we don't need the loop variable.
even_numbers = []
for _ in range(5):
	n = int(input("Enter a number: "))
	if n % 2 == 0:
		even_numbers.append(n)
print("Even numbers:", even_numbers)