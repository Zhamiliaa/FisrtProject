#
#
# data = [
#     {'text':'oh hi duuuude how r uy??check this 1xbet'},
#     {'text':'Dear Harry Potter, i am Frodo Baggins i represent 1xbet company.Best bet service'},
#     {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
#     {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
# ]
# final_mail = 'Hello Harry, my name is Maksim, Im still waiting for the letter from Hogwarts'
#
# q_spam = 0
# database = []
# spam_word = ''
#
# for mail in data:
#     str = mail['text'].split()
#     database.extend(str)
#
# for word in database:
#     quantity = database.count(word)
#     if quantity > q_spam:
#         q_spam = quantity
#         spam_word = word
#
# if spam_word in final_mail:
#     print('mail is not OK!')
# else:
#     print('mail is OK!')


# """
# users:
#     sale - скидка на любую покупку в %
#     status - юридическое или частное лицо
# purchases:
#     taxes - процентная ставка налога на всю покупку,
#
# Описание проблемы:
# Большая часть базы данных удалилась, по имеющейся информации вычислить сколько люди потратили на уцелевшие покупки
# Задание:
# 1. Вычислить сколько потратил каждый покупатель с оплатой налогов
# 2. Для пользователей у кого незаполнено поле total_amount - вычислить по имеющимся покупкам
# 3. Текущую общую стоимость записать в файл (Имя + потраченные деньги)
# """
#
#
# users = [
#     {'id':1,'username':'superman','country':'Crypton','total_amount':57890,'sale':10,'status':'gov'},
#     {'id':2,'username':'Bruce Wayne','country':'USA','total_amount':1000000000,'sale':67,'status':'private'},
#     {'id':3,'username':'joker','country':None,'total_amount':None,'sale':None,'status':'private'},
#     {'id':4,'username':'jamilya','country':'Kyrgyzstan','total_amount':777000,'sale':30,'status':'gov'},
#     {'id':5,'username':'aliya','country':'Kyrgyzstan','total_amount':777000,'sale':31,'status':'gov'},
#     {'id':6,'username':'cr7','country':'Portugal','total_amount':None,'sale':50,'status':'private'},
#     {'id':7,'username':'trump','country':'USA','total_amount':1000000000,'sale':0,'status':'gov'},
#     {'id':8,'username':'cholpon','country':'Kyrgyzstan','total_amount':200000,'sale':10,'status':'private'},
# ]
#
# purchases = [
#     {'id':1,'user_id':1,'products':['glasses','cloak','coat'],'taxes':21},
#     {'id':2,'user_id':2,'products':['washington_post','spaceX','gotham'],'taxes':56},
#     {'id':3,'user_id':2,'products':['daily planet','bicycle'],'taxes':18},
#     {'id':4,'user_id':2,'products':['factory','amazon','coat'],'taxes':70},
#     {'id':5,'user_id':3,'products':['grenade','machine gun'],'taxes':1},
#     {'id':6,'user_id':4,'products':['glasses','cloak','coat'],'taxes':23},
#     {'id':7,'user_id':4,'products':['glasses','cloak','coat'],'taxes':29},
#     {'id':8,'user_id':5,'products':['glasses','cloak','coat'],'taxes':41},
#     {'id':9,'user_id':5,'products':['glasses','cloak','coat'],'taxes':23},
#     {'id':10,'user_id':6,'products':['glasses','cloak','coat'],'taxes':24},
#     {'id':11,'user_id':6,'products':['glasses','cloak','coat'],'taxes':11},
#     {'id':12,'user_id':7,'products':['glasses','cloak','coat'],'taxes':0},
#     {'id':13,'user_id':8,'products':['glasses','cloak','coat'],'taxes':7},
#     {'id':14,'user_id':8,'products':['glasses','cloak','coat'],'taxes':7},
#     {'id':15,'user_id':7,'products':['glasses','cloak','coat'],'taxes':1},
# ]
# products = {'glasses':23000,'cloak':17000,'coat':16000,
#             'washington_post':1000000,'spaceX':9999999,'gotham':None,
#             'daily planet':1800000,'bicycle':1000,'factory':780000,'amazon':None,
#             'grenade':8000,'machine gun':71000}
#
# products.pop('adasdsa','None')
#
# def to_file(data):
#     file1 = open('test, txt', 'w')
#     for user in data:
#         result_str = "{} : {}".format(user['username'], user['total_amount'])
#         file1.write(result_str + '/n')
#     file1.close()
#
#
# to_file(users)

dict1 = {'a':1, 'b': 3, "n": 6}
dict2 = {'c':33, 'w':2, 'x':2}

dict1.update(dict2)
print(dict1)














