# my_list = [1,2,3,4,5]
# print(type(my_list))
#
# my_tuple = (1,2,3,4,5,6)  #неизменяемый список, могут нах-ся разные типы данных как и в списке
# print(type(my_tuple))

# criminals = ['johny', 'sparrow','harry','potter','jcvd','selena']
#
# name = input()
#
# if name not in criminals:
#     criminals.append(name)
# print(criminals)

import random
database = [['maksim'],['123456']]

username = input("Enter username: ")
password = input("Enter password: ")
check_password = input("Enter check_password: ")
if len(username) > 8 and len(password) >= 6:
    if password == check_password:
        secret = random.randint(1000,9999)
        print(secret,'security code')
        code = int(input())
        if code == secret:
            database[0].append(username)
            database[1].append(password)
        else:
            print('Incorrect code!!')
    else:
        print('password dont match!')
print(database)
print("Please log in")
tries = 0
stop = None
while tries < 3:
    count = 0
    username = input("Enter username: ")
    password = input("Enter password: ")

    while count < len(database[0]):
        if username == database[0][count] and password == database[1][count]:
            print('okay!')
            break
        else:
            print('Not okay!')
        count += 1
    tries += 1



