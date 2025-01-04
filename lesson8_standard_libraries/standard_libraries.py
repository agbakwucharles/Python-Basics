import os
import sys
import math
import datetime
import random

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Get the Python version
python_version = sys.version
print(f"Python version: {python_version}")

# Calculate the square root of 16
sqrt_16 = math.sqrt(16)
print(f"Square root of 16: {sqrt_16}")

# Get the current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")