# Introduction to List:
# a = [11, 15, 1.5, 40, "Potato"]
# print(a[3])
# print(a[4])

# a[4] = "Onion"
# print(a)

# More about indexing
# a = [12, 20, 34, "Phitron"]
# print(a[3])
# print(a[-4])


# print(len(a))
# a[-3] = 300 # Changed in memory

# if 300 in a:
#     print("Found")
# else:
#     print("Not found")
# print(a)



# *** Traversing **
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# for i in range(-1, -len(a)-1, -1):
#     print(a[i])

# for i in range(len(a)-1, -1, -1):
#     print(a[i])



# *** List Slicing ***
# a = [12, 13, 4, "Orange", "Mango", [12.5, 19]]
# print(a[::])
# print(a[1::])
# print(a[2::2])
# print(a[::-1]) # New technic of list reverse
# print(a[-1:-3:-1])
# print(a[-1:-1:-1]) # []

# *** List build in methods ***
# a = [1,2,3]
# b = [4,5, 6]
# c = a + b
# print(c)

# list() convert string to list
# s = "Hello World!"
# print(list(s))


# append() adds an element at the end of a list
# a = [12, 45, 56]
# a.append(22)
# print(a)


# insert() adds an element at a specified position
# a = [1, 2, 3,4,5]
# a.insert(2, 100)
# print(a)


# copy() returns a copy list of a list
# a = [1, 2, 3,4,5]
# b = a.copy()
# print(a)



# count() returns the number of elements of with the specified value
# a = [1, 2, 2, 2, 2, 5, 5, 4]
# print(a.count(2))


# extend() adds the elements to a list at the end in the current list
# a = [12, 2, 5, 5, 6]
# a.extend([2,3])
# a = a + [2, 3]
# print(a)



# pop() removes and returns the last value from the list the given index value.
# a = [12, 2, 5, 5, 6]
# a.pop()
# poped_value = a.pop()
# print(a)



# remove() removes a given object from the list
# a = [12, 2, 5, 5, 6]
# a.remove(12)
# print(a)


# clear() removes all the elements from a list
# a = [12, 2, 5, 5, 6]
# a.clear()
# print(a)



# reverse() reverses objects of the list in place
# a = [12, 2, 5, 5, 6]
# print(a[::-1])
# a.reverse()
# print(a)



# sort() sort a list in ascending, descending 
# a = [12, 2, 5, 5, 6]
# # a.sort()
# a.sort(reverse=True)
# print(a)


# max() calculates the max value of a list
# a = [12, 2, 5, 5, 6]
# print(max(a))
# print(min(a))




# Taking multiple inputs from user and store them in a list

# Problem - 1: Taking multiple string inputs
# a = input().split()
# print(a)

# Problem - 2: Taking multiple int inputs
# a = list(map(int, input().split())) # map(ki korbo, kar upor korbo)
# print(a)

# Problem - 3: Taking multiple float inputs
# a = list(map(float, input().split()))
# print(a)