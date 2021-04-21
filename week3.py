# numbers = [10, 20, 30, 40, 7, 8, 9, 1, 2, 3, 4]
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# try:
#     print('1'+'1')
# except TypeError:
#     print('except')
# finally:
#     print('finally')

# names = ['vladimir', 'zhamilia', 'cholpon', 'begimai', 'erbol', 'bakyt', 'aliya']
# salaries = [0, 10000, 20000, None, 30000, None, None]
#
# i = 0
# while i < len(names):
#     try:
#         salaries[i] *= 2
#     except TypeError:
#         salaries.append(0)
#     i += 1
#
# print(salaries)


data = [
    {'dress':[
                {'name':'louis vuitton',
                'popularity':500,
                 'price':1000
                },
                {'name':'versace',
                'popularity':21,
                 'price':888
                },
                {'name':'supreme',
                'popularity':57,
                 'price':765
                },
    ]
    },
    {'jeans':[
                {'name':'adidas',
                'popularity':42,
                 'price':2300
                },
                {'name':'armani',
                'popularity':678,
                 'price':110
                },
                {'name':'casio',
                'popularity':230,
                 'price':3000
                },
    ]
    },
    {'t-shirt':[
                {'name':'tom ford',
                'popularity':999,
                 'price':5000
                },
                {'name':'lacoste',
                'popularity':777,
                 'price':230
                },
                {'name':'luxury',
                'popularity':876,
                 'price':2300
                },
    ]
    }
]

list1 = ['dress', 'jeans', 't-shirt']

i = 0
category_price = {}

for category in data:
    category_sum = 0
    key = list1[i]
    category_value = category[key]
    for product in category_value:
        category_sum += product['price']
    category_price[key] = category_sum
    i += 1

print(max(category_price.values()), category_price)


list1 = ['dress', 'jeans', 't-shirt']

i = 0
category_popular = {}

for popularity in data:
    popular_sum = 0
    key = list1[i]
    popularity_value = popularity[key]
    for most_popular in popularity_value:
        popular_sum += most_popular['popularity']
    category_popular[key] = popular_sum
    i += 1

print(max(category_popular.values()),category_popular)

list1 = ['dress', 'jeans', 't-shirt']

i = 0
price_list = []

for category in data:
    # print(category)
    key = list1[i]
    value = category[key]
    # print(value)
    for product in value:
        price_list.append(product['price'])
    i += 1
file1 = open('test.txt', 'w')
file1.write(str(max(price_list)))














