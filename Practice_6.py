# Function to calculate the square of a number
def square_number(n):
    return n * n

# Input from the user
num = float(input("Enter a number: "))

# Calculate the square and display the result
square_result = square_number(num)
print(f"The square of {num} is {square_result}.")
