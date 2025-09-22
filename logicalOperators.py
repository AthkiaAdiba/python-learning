# Python logical operators ---> Work with boolean values
# and
# or
# not

print(10 - 6 == 4 and 10 - 5 == 15)
print(10 - 6 == 4 and 10 - 5 == 5)

print(10 - 6 == 4 or 10 - 5 == 15)
print(10 - 6 == 4 or 10 - 5 == 5)

print(not(10 - 6 == 4))

# Problem - 1

marks = 75

if marks >= 90 and marks <= 100:
    print("you will get two candy")
elif marks >= 80 and marks <= 90:
    print("You will get one candy.")
else: 
    print("You will not anything.")