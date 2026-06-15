# Name: Deeksha sethi
# Project name: Personal Information Manager
# Description: This Python program stores and displays personal information using variables, user inputs, string formatting and basic input validation.

# Welcome Message
print("-"* 60)
print("Welcome to the Personal Information Manager")
print("-"* 60)

# Store information
print("Information: \n")
name="deeksha sethi"    # name is a string variable 
age=19                  # age is a int variable
city="faridabad"        # city is a string variable
hobby="writing"         # hobby is a string variable

# Get user info and store it in variables
print("Enter the following details: ")
fav_food=input("Enter your favorite food: ")
while(fav_food.strip()==""):
    print("Enter a valid input!")
    fav_food=input("Enter your favorite food: ")
fav_color=input("Enter your favorite color: ")    
while(fav_color.strip()==""):
    print("Enter a valid input!")
    fav_color=input("Enter your favorite color: ")
print()

# Calculate age in months
age_months=age*12

# Display information
print("-"* 60)
print()
print("Your Basic Information\n")
print("Your Details\n")
print(f"Name: {name.title()}")
print(f"Age: {age} and age in months :{age_months}")
print(f"City: {city.title()}")
print(f"Hobby: {hobby.title()}")
print()
print("Your Entered Information\n")
print(f"Favorite food: {fav_food.title()}")
print(f"Favorite color: {fav_color.title()}")  
print()

# A Goodbye message
print("-"* 60)
print("Thank you for using Personal Information Manager...")
print("-"* 60)

# End of the program