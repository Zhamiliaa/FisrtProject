# numbers = [1,7,4,10,9,8,20,21,25,1,3,0]

# print(sum(numbers))
# # print(max(numbers))
# print(min(numbers))

# max_number = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#         print(max_number)
#     i += 1
# print(max_number)
#
# i = 0
# sum = 0
# while i < len(numbers):
#     sum += numbers[i]
#     i += 1
#
# print(sum)

#
# numbers = [1,7,4,10,9,8,20,21,25,1,3,0]
#
# i = 0
# max_num = 0
#
# while i < len(numbers):
#     if numbers[i] > max_num:
#         max_num =numbers[i]
#     i += 1
#
# second = 0
# i = 0
#
# while i < len(numbers):
#     if numbers[i] > second < max_num:
#         second = numbers[i]
#     i += 1
# print(max_num, second)

# numbers = [1,7,7,7,8,9,10,12,14,7,6,3,4,7,1,0]
# gt_ten = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         gt_ten += 1
#     i += 1
# print(gt_ten)


# numbers = [1,7,7,7,8,9,10,12,14,7,6,3,4,7,1,0]
# uniq_numbers = []
# i = 0
#
# while i < len(numbers):
#     if numbers[i] not in uniq_numbers:
#         uniq_numbers.append(numbers[i])
#
#     i += 1
#     uniq_numbers.sort()
# print(uniq_numbers)

# numbers = [3,5,8,0,11,2,6,23,4]
# # print(max(numbers))
#
# max_number = 0
# i = 0
#
# while i < len(numbers):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#
#     i += 1
# print(max_number)

# numbers = [3,5,8,0,11,2,6,23,4]
# numbers.reverse()
# print(numbers)

# numbers = [3,5,8,0,11,2,6,23,4]
#
# max_num = 0
# i = 0
#
# while i < len(numbers):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#
#     i += 1
# print(max_num)
# print(numbers.index(max_num))

# numbers = [3,5,8,0,11,2,6,23,4]
# numbers.insert(1,'C')
# print(numbers)

# numbers = [3,5,8,0,11,2,6,23,4]
# numbers.pop(2)
# print(numbers)



# numbers = [3,5,-8,0,-11,2,-6,-23,4]

# i = 0
# positive = 0
# negative = 0
#
# while i < len(numbers):
#     if numbers[i] > 0:
#         positive = positive + 1
#
#     if numbers[i] < 0:
#         negative = numbers[i]
#
#     i += 1
# print(positive,negative)


# numbers = [1,2,3,4,5,6]

# for i in numbers:
#     print(i)

# for i in range(100):
#     print(i)

# numbers1 = range(100)
# print(type(numbers1))
#
# numbers = ['red','yellow','green','blue']
# for i in range(0,len(numbers),2):
#     print(numbers[i])

# for i in range(1,1000,1):
#     print(i)

import random

# random_numbers = [1, 2, 3.2, 4, 'fyfuf', [1,2,3], 'otot', 'gkkg', 1]

# for i in random_numbers:
#     if isinstance(i, int) or isinstance(i, float):
#         print(i ** 2)

# sum = 0
# nested_sum = 0
# for i in random_numbers:
#     if isinstance(i,int) or isinstance(i,float):
#         sum += i
#     elif isinstance(i,list):
#         for j in i:
#             nested_sum += i
#         print(nested_sum)


# string1 = 'hello'
# print(string1[0])

# article ='ooJKLoo ooOooo'
# print(article.isupper())
# print(article.islower())
# article = article.lower()
# print(article)

# print(article.isalnum()) либо цифры либо буквы либо вместе без пробелов и знаков

# article = article.endswith('bakyt')
# article = article.startswith('hgggjj')
# print(article.find('jama')
# print(article)

# article = article.strip()
# print(article)

# article = article.capitalize()
# print(article)

# article = article.title()
# print(article)

# print(article.index('l'))

# article = 'Vasya is the best actor, Vasya is rich'
# # article = article.swapcase()
# # article = article.split()
# # article = article.replace('Vasya', 'Petya',1)
# print(article)











