# Introduction string in Python
a = "Hello World"
b = 'Hello World'
c = """ This is a 
multiple 
line
string
"""



# *** Indexing and immutability in Python ***
# a = "Hello World"
# print(a[4])
# print(a[-4])

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i], end= " ")

# print(a[2:10:3])





# *** String methods part - 1:

# lower(): converts characters into lower case
# a = "Hello World Python"
# print(a.lower())



# upper(): Converts characters into upper case
# a = "Hello World Python"
# print(a.upper())



# title(): Converts characters into title case
# a = "Hello World Python"
# print(a.title())



# isupper()
# islower()
# istitle()
# isalpha()
# print("aedd123".isalpha())





# *** String methods part - 2:
a = "Hello World Python"

# capitalize()
# print(a.capitalize())


# title()
# print(a.title())


# swapcase()
# print(a.swapcase())


# casefold() text = 'groB'
# replace()
# b = 'helle'
# c = b.replace(b[4], 'o', 1)
# print(c)


# count()
# print(a.count('h'))


# isdigit()
# join()
# a = ['h', 'e', 'l', 'l', 'o']
# print(''.join(a))

# split()
# a = 'hello'
# print(a.split(" "))
# print(list(a))





# More about string in python
# *** String formatting ***
# Method - 1:
# name = 'Tonne'
# age = 18
# template_string = 'I am {}. I am {} years old.'.format(name, age)
# template_string = 'I am {1}. I am {0} years old.'.format(age, name)
# print(template_string)
# template_string = 'I am {name}. I am {age} years old.'.format(age = 20, name = 'Tonne')
# print(template_string)


# Method - 2:
# name = 'Tonne'
# age = 18

# string = f"I am {name}. I am {age+20} years old."
# print(string)






# *** String concatenation ***
# a = 'Hello'
# b = 'World'
# c = a + " " +b
# print(c)
# 2^3 = 2 * 2 * 2
print('hello '* 3)