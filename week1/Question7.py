# Distribute Items Equally (Candies among Students):

# Input number of candies and students
candies = int(input("Enter the total number of candies: "))
students = int(input("Enter the number of students: "))

# Calculate how many each student gets and how many are left
each_gets = candies // students
leftover = candies % students

# Display the results
print(f"\nEach student gets: {each_gets} candies")
print(f"Remaining candies: {leftover}")
