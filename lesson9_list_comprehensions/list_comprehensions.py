# List comprehensions examples

# Example 1: Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Example 2: Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

# Example 3: Create a list of tuples (number, square) for numbers from 1 to 5
number_square_tuples = [(x, x**2) for x in range(1, 6)]
print("Number-Square Tuples:", number_square_tuples)

# Example 4: Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print("Flattened List:", flattened_list)

# Example 5: Create a list of uppercase characters from a string
input_string = "hello"
uppercase_chars = [char.upper() for char in input_string]
print("Uppercase Characters:", uppercase_chars)