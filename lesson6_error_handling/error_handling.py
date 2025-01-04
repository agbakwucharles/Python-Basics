def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    else:
        return result
    finally:
        print("Execution completed.")

# Example usage
print(divide_numbers(10, 2))  # Should print 5.0
print(divide_numbers(10, 0))  # Should print error message for division by zero
print(divide_numbers(10, 'a'))  # Should print error message for type error