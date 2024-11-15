# PART 1
# Greet the user and ensure their name starts with a capital letter.

print("Hello! I am a program that handles integers.")

# Ask for the user's name
user_name = input("Please enter your name:\n")

# Capitalize the first letter of the name if necessary
if not user_name[0].isupper():
    user_name = user_name.capitalize()
    print("The first letter of your name was corrected to uppercase.")
else:
    print("Welcome,", user_name)

# PART 2
# Request two integers separated by a comma and a third integer in a separate input
numbers_input = input("Enter two numbers separated by a comma:\n")
numbers_split = numbers_input.split(',')

# Convert the inputs into integers
num1 = int(numbers_split[0])
num2 = int(numbers_split[1])

# Ask for the third number
num3 = int(input("Please enter the third number:\n"))

# Store the numbers in a list
number_list = [num1, num2, num3]

# Print the numbers one by one
print("The numbers you entered are:")
print(number_list[0])
print(number_list[1])
print(number_list[2])

# Calculate and print the average
average = sum(number_list) / 3
print("The average of the numbers is:", average)

# PERFORM CHECKS
# 1. Check if the third number is greater than the sum of the first two
if num3 > num1 + num2:
    print("The third number is greater than the sum of the first two numbers.")
else:
    print("The third number is not greater than the sum of the first two numbers.")

# 2. Check if all three numbers are unique
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All the numbers are different.")
else:
    print("Not all the numbers are different.")

# 3. Check if the sum of the three numbers is greater than the length of the user's name
if sum(number_list) > len(user_name):
    print("The sum of the three numbers is greater than the number of characters in your name.")
else:
    print("The sum of the three numbers is not greater than the number of characters in your name.")
