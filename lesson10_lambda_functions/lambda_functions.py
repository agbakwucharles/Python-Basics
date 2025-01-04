# Example of a lambda function that adds 10 to the input number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Example of a lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# Example of a lambda function used with the `sorted` function
points = [(1, 2), (3, 1), (5, -1), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2), (2, 3)]

# Example of a lambda function used with the `map` function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example of a lambda function used with the `filter` function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]