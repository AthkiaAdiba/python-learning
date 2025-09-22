# Problem - 1: Python programme to print a multiplication table of a given number
# a = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(a, "X", i, " = ",  a*i)

# Problem - 2: Python programme to find the factorial of a given number.
# a = int(input("Enter a value: "))
# factorial = 1

# for i in range(1, a+1):
#     factorial = factorial * a

# print(factorial)


# Problem - 3: 
# fibonacci series
# a = 0
# b = 1
# or
# a, b = 0, 1

# for i in range(10):
#     print(a, end=" ")
#     result = a + b
#     a = b
#     b = result

# Problem - 4:Count the number of digit in a number
# Method 1: Longway

# a = int(input("Enter a number: "))
# count = 0

# while a > 0:
#     digit = a % 10
#     count = count + 1
#     a = a // 10

# print(count)

# Method 2: Shortcut
# b = input()
# print(len(b))


# Problem - 5: Python programme to check Armstrong number
# Method 1:

# a = int(input("Enter a number: "))
# num_length = len(str(a))
# temp = a
# sum = 0

# while temp>0:
#     lst_digit = temp % 10
#     sum = sum + lst_digit ** num_length
#     temp = temp // 10

# if a == sum:
#     print("It is a Armstrong number.")
# else:
#     print("It is not a Armstrong number.")

# Method 2:
# a = input()
# num_length = len(a)
# sum = 0

# for i in a:
#     sum = sum + int(i) ** num_length

# if int(a) == sum:
#     print("It is a Armstrong number.")
# else:
#     print("It is not a Armstrong number.")


# Problem - 6: Integer number reverse
# a = int(input("Enter a number: "))
# rev_a = 0

# while a>0:
#     last_digit = a % 10
#     rev_a = rev_a * 10 + last_digit
#     a = a // 10

# print(rev_a)