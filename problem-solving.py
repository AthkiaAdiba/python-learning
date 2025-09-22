# Problem - 1 : Take two values of length and breadth of a rectangle from user and check if it is square or not.

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# if length == breadth:
#     print("This is a square.")
# else: 
#     print("This is a rectangle.")


# Problem - 2 : Take three integer input from user find the largest number between using if-elif-else statement

# Method 1 : Using nested if concept
# number1 = int(input("Enter the number 1: "))
# number2 = int(input("Enter the number 2: "))
# number3 = int(input("Enter the number 3: "))

# if number1 > number2: 
#     if number1 > number3: 
#         print(number1, "is the largest.")
#     else: 
#         print(number3, "is the largest.")
# else: 
#     if number2 > number3: 
#         print(number2, "is the largest.")
#     else: 
#         print(number3, "is the largest.")

# Method 2 : using logical operator

# if number1 > number2 and number1 > number3: 
#     print(number1, "is the largest.")
# elif number2 > number1 and number2 > number3: 
#     print(number2, "is the largest.")
# else: 
#     print(number3, "is the largest.")

# Problem - 3 : Write a programme using conditional statement wether a number is even or odd.

# a = int(input("Enter  number: "))

# if a % 2 == 0:
#     print(a, "an even number.")
# else: 
#     print(a, "an odd number.")

# Problem - 4 : Write a programme to take integer input from user and display the grade according to the following criteria.

# >90  ---> A
# >80 and <=90  ---> B
# >=60 and <=80  ---> C
# Below 60  ---> D

# marks = int(input("Please enter your marks: "))

# if marks > 90:
#     print("Your grade is A.")
# elif marks > 80 and marks <= 90:
#     print("Your grade is B.")
# elif marks >= 60 and marks <= 80:
#     print("Your grade is C.")
# else: 
#     print("Your grade is D.")

# Problem - 5 : Write a programme to check a year is leap year or not. Take input from user.

# Method 1:

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("This year is leap year.")
# elif year % 100 == 0:
#     print("This year is not leap year.")
# elif year % 4 == 0: 
#     print("This year is leap year.")
# else: 
#     print("This year is not leap year.")

# Method - 2:
# if year % 400 == 0 and year % 100 == 0:
#     print("This year is leap year.")
# elif year % 4 == 0 and year % 100 != 0:
#     print("This year is leap year.")
# else: 
#     print("This year is not leap year.")

# Method - 3:
# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print("This year is leap year.")
# else: 
#     print("This year is not leap year.")