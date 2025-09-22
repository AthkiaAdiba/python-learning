# List Comprehension: Part - 1

# [expression for item in list]

# Example 1: Iteration with list comprehension
# a = [10, 20, 30, 40, 50]
# b = [i + 5 for i in a]
# print(b)


# Example 2: Iterating through a string using list comprehension
# a = "Hello World"
# b = [i for i in a]
# print(b)


# Example 3: Using range() function in list comprehension
# a = [i for i in range(1, 20, 2)] # 1 3 5 7 9
# a = [i for i in range(2, 20, 2)] # 2 4 6 8 10
# print(a)




# List Comprehension: Part - 2

# [expression(element) for element in list if condition]


# Example 4: Using if with list comprehension
# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#         a.append(i)
# print(a)
# ------------------
# b = [i for i in range(1, 20) if i % 3 == 0]
# print(b)



# Example 5: Nested if with list comprehension

# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#         a.append(i)
#     if i % 5 == 0:
#         a.append(i)
# print(a)

# -------------------
# b = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0]
# print(b)

# Example 6: if...else with list comprehension

# a = []
# for i in range(1, 20):
#     if i % 2 == 0:
#         a.append("Even")
#     else:
#         a.append("Odd")

# print(a)

# -------------------
# b = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 20)]
# print(b)

# [if else for i in list]




# *** 2D List Comprehension ***
matrix = [[1,2], [3, 4], [5, 6], [7, 8]]
# Transpose matrix a conversion

# a = []
# for row in range(2):   # Outer loop
#     b = []
#     for col in matrix:  # Inner loop
#         b.append(col[row])
#     a.append(b)

# print(a)

# res = [[col[row] for col in matrix] for row in range(2)]
# print(res)
