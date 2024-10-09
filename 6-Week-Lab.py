# Exercise 1 - File Display
#
# # open the File
# file = open('numbers.txt', 'r')
#
# # Read and display the file's contents
# for line in file:
#     number = int(line)
#     print(number)
#
# # Close the file
# file.close()

# --------------------------------------------------------------

# Exercise 2 - File Head Display

# Ask for the file name
# file_name = input("What is the name of the file? ")
#
# # Open the file in read mode
# file = open(file_name, 'r')
#
# # Read all lines from the file
# lines = file.readlines()
#
# # Initialize a line counter
# line_count = 0
#
# for line in lines:
#     # Check if we have printed less than 5 lines
#     if line_count < 5:
#         print(line.strip())  
#         line_count += 1  # Increment the line counter
#     else:
#         break 
#
# # Close the file
# file.close()

# --------------------------------------------------------------

# Exercise 3 - Line Numbers

# # Ask for the file name
# file_name = input("What is the name of the file? ")
#
# # # Open the file in read mode
# file = open(file_name, 'r')
#
# # Read all lines from the file
# lines = file.readlines()
#
# # Initialize a line counter
# line_count = 0
#
# # Gets line number and prints contents - 1: Hello
# for line in lines:
#     line_count += 1
#     print(f'{line_count}: {line.strip()}')
#
# # Close the file
# file.close()

# --------------------------------------------------------------

# Exercise 4 - Item counter

# # Ask for the file name
# file_name = input("What is the name of the file? ")
#
# # # Open the file in read mode
# file = open(file_name, 'r')
#
# # Read all lines from the file
# lines = file.readlines()
#
# # Initialize a line counter
# line_count = 0
#
# # loops through file if line is stripped add it to line_count 
# for line in lines:
#     if line.strip():
#         line_count += 1
#
# # Close the file
# file.close()
#
# # Display total names
# print(f"The total number of names in the file is: {line_count}")

# --------------------------------------------------------------

# Exercise 5 - Sum of Numbers

# Open the file
file = open('test.txt', 'r')

# Read the file lines
lines = file.readlines()

# Initialize Total
total = 0

# Loops through each line chages it to a int, prints line, adds the value to total 
for line in lines:
    line = int(line)
    print(line)
    total += line 

# Close the file
file.close()

print(f"The total in the file numbers.txt is: {total}")



















