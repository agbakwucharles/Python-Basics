# if-elif-else statement
def check_number(num):
    if num > 0:
        return "Positive number"
    elif num == 0:
        return "Zero"
    else:
        return "Negative number"

# for loop
def print_numbers(n):
    for i in range(n):
        print(i)

# while loop
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

# Example usage
if __name__ == "__main__":
    print(check_number(10))
    print_numbers(5)
    countdown(5)