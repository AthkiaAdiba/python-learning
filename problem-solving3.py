# Problem - 1: swapping two list elements
# a = [17, 12, 13, 15, 16, 10]
# temp = a[0]
# a[0] = a[-1] # a[len(a) - 11]
# a[-1] = temp
# print(a)





# Problem - 2: Count unique elements in a list
# a = [1, 2, 2, 3, 3, 3, 4, 5, 6]
# b = []
# count = 0

# for i in a:
#     if i not in b:
#         count += 1
#         b.append(i)
# print(count)
# print(b)




# Problem - 3: Given a list, extract all elements whose frequency is greater than k. Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], k = 3. Output: [4, 3]

# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k = 3
# result = []

# for i in test_list:
#     freq = test_list.count(i)
#     if freq > k and i not in result:
#         result.append(i)

# print(result)




# Problem - 4: Create the following list using list comprehension
# [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
# a = [[j for j in range(5) if i != j ] for i in range(5)]
# print(a)