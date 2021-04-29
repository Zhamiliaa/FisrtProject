# def maximum_of_list(numbers):
#     return max(numbers)
#
# print(maximum_of_list([1,2,3,4,5]))
# print(maximum_of_list([29,4,56,90]))

# def maximum_of_2():
#     num1 = int(input())
#     num2 = int(input())
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)
#
#
# def register(username,password,confirm_password):
#     if password == confirm_password:
#         return username,password
#     else:
#         print('paroli ne sovpadayut')
#


#
# def register(username, password, confirm_password):
#     if password == confirm_password  and len(username) >= 8 and not password.isalpha():
#         return username, password
#
# try:
#     username, password = register('harry', '123456', '123456')
#     print('регистрация завершена')
# except TypeError:
#     print('введите правильные данные')
#
# def auth():
#     for i in range(3):
#         username1 = input()
#         password1 = input()
#         if username == username and password1 == password:
#             print('ok!')
#             break
#         else:
#             print('not ok!')
# auth()

# def autorize(check_username, check_password):
#     if check_username == username and check_password == password:
#         print('autorize')
#
#     else:
#         print('autorize is failed!')
#
#
# autorize('harry','23456')


# data = {
#     'glock.20': 2000,
#     'usp': 2500,
#     'fs': 3467,
#     'deagle': 5000,
#     'p92': 4000,
#     'colt': 90000,
#     'magnum': 6000,
#     'p90': 10000,
#     'mp7': 11000,
#     'uzi': 12000,
#     'mp5': 14000,
#     'm16': 20000,
#     'ak-47': 19000,
#     'm416': 24000,
#     'famas': 21000,
#     'AWM': 30000,
#     'Dragunov': 31000,
#     'Barett': 50000,
#     'RPG': 100000,
#     'Topol-M': 2000000
# }
#
# """
# ТЗ:
# По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
# Если товар в списке отсутствует - NOT OK
# __________
# Входные данные: название товара,кол-во товара, наличные
# Реализовать 2+ функциями
# Выходные данные: словарь состящий из:
# {названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
# """
#
#
# weapon = input()
# quantity = int(input())
# money = int(input())
# def count_payback(price,quantity,money):
#     payback = quantity * price
#     if money >= payback:
#         return money - payback
#     else:
#         return 'Недостаточно средств'
# def shop(weapon_name,quantity,money):
#     if weapon_name in data:
#         price = data[weapon_name]
#         payback = count_payback(price,quantity,money)
#         if isinstance(payback,int):
#             result = {'weapon_name':quantity,'total_sum':price*quantity}
#         else:
#             result = payback
#         print(result)
#     else:
#         print('We have no {}!'.format(weapon_name))
# shop(weapon,quantity,money)

#
#
#
# blogs = [{'id':1,'title':'MyFirstBlog','description':'lalal2'},
#         {'id':2,'title':'Travel','description':'lalal2'},
#         {'id':3,'title':'Food','description':'lalal2'},
#         {'id':4,'title':'Music','description':'lalal2'},
#         {'id':5,'title':'Movies','description':'lalal2'},
#         {'id':6,'title':'Books','description':'lalal2'},
#         ]
# posts = [
#     {'id':1,'blog_id':1,'subject':'learn python','text':'wooh','rate':9.8},
#     {'id':2,'blog_id':1,'subject':'develop program','text':'wooh','rate':7},
#     {'id':3,'blog_id':1,'subject':'learn framework','text':'wooh','rate':10},
#     {'id':4,'blog_id':2,'subject':'mountain','text':'wooh','rate':3},
#     {'id':5,'blog_id':3,'subject':'fast-food','text':'wooh','rate':8.9},
#     {'id':6,'blog_id':4,'subject':'rock!','text':'wooh','rate':5.7},
#     {'id':7,'blog_id':2,'subject':'lakes','text':'wooh','rate':1.2},
#     {'id':8,'blog_id':3,'subject':'plov','text':'wooh','rate':7},
#     {'id':9,'blog_id':6,'subject':'ABC','text':'wooh','rate':10},
#     {'id':10,'blog_id':2,'subject':'woods','text':'wooh','rate':2.1},
#     {'id':11,'blog_id':3,'subject':'pizza','text':'wooh','rate':4.2},
#     {'id':12,'blog_id':4,'subject':'classic','text':'wooh','rate':6.6},
#     {'id':13,'blog_id':5,'subject':'Lord of The Rings','text':'wooh','rate':10},
#     {'id':14,'blog_id':5,'subject':'Wrath of Man','text':'wooh','rate':0.9},
# ]
#
# """
# blog_id - идентификатор к какому блогу относится данный post
# Задание:
# 1.Вычислить какой блог самый топ, а какой нет - ориентируясь на поле rate в post
#     1.1. Для этого - требуется вычислить для каждого блога - среднюю оценку всех его post
# 2. Вычислить самый популярный post - если с такой оценкой их несколько - вывести все
# """
# max = 0
# for blog in blogs:
#     avg_sum = 0
#     i = 0
#     for post in posts:
#         if blog['id'] == post['blog_id']:
#             avg_sum += post['rate']
#             i += 1
#     avg_rate = avg_sum / i
#     blog['avg_sum'] = avg_rate
#
#     if blog['avg_sum'] > max:
#         max = blog['avg_sum']
#         print(max, blog)
#
# for post in posts:
#     rate = post['rate']
#     if rate == max:
#         print(max, post)

data = [
    {'user': 'digital', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'sam', 'email': 'digital', 'age': 23, 'salary': 200000, 'department': 'manager'},
    {'user': 'john', 'email': 'john@google.com', 'age': 23, 'salary': 200000, 'department': 'CEO'},
    {'user': 'sparrow', 'email': 'digital@go.com', 'age': 23, 'salary': 200000, 'department': 'SEO'},
    {'user': 'orlando', 'email': 'digital@gmail.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'ben', 'email': 'digi', 'age': 23, 'salary': 200000, 'department': 'worker'},
    {'user': 'stiller', 'email': 'digital@apple.com', 'age': 23, 'salary': 200000, 'department': 'loan'},
    {'user': 'adam', 'email': 'email@email.com', 'age': 23, 'salary': 200000, 'department': 'credit'},
    {'user': 'eva', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'buying'},
    {'user': 'frodo', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'harry', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'ron', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'germiona', 'email': 'digit', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'gannibal', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'lector', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'}
]
worker_of_month = {'IT': ['adam', 'sparrow', 'ben', 'frodo', 'gannibal'],
                   'credit': [],
                   'loan': ['stiller'],
                   'food': ['gannibal', 'lector']}
"""
1.Всем работникам месяца увеличить зарплату на 10%
2.Отделу где больше одного работников месяца увеличить зарплату на 5% дополнительно
3.Отдел где нет работников месяца - уменьшить всем зарплату на 3%
4.Работники чьи email-не принадлежат гуглу все кроме [@google.com,@gmail.com] - уволить
"""

# for worker in worker_of_month:
#     workers = 0
#
#     for user in data:
#         if user['department'] == worker:
#             workers = user['salary'] /100 * 10 + user['salary']
#             print(workers,user['department'])

def worker_of_month_increase_salary(data, worker_of_month):
    for worker_key,worker_value in worker_of_month.items():
        for worker in worker_value:
            for user in data:
                if user['user'] == worker:
                    user['salary'] = user['salary'] + (user['salary'] * 0.1)
    return data

data = worker_of_month_increase_salary(data,worker_of_month)


def best_departments(data,worker_of_month):
    for worker_key, worker_value in worker_of_month.items():
        for worker in worker_value:
             if len(worker_value) > 1:
                 for user in data:
                     if user['user'] == worker:
                         user['salary'] = user['salary'] / 100 * 5 + user['salary']

    return data

data = best_departments(data,worker_of_month)


def remove_worker(data = data):
    data_copy = data.copy()
    for user in data_copy:
        email = user['email']
        if '@google.com' in email or '@gmail.com' in email:
            pass
        else:
            data.remove(user)
    return data
data = remove_worker(data=data)





































