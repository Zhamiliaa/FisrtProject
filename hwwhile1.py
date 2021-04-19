# count = 0
# sum = 0
# while count < 100:
#     # count = count + 1
#     count += 1
#     sum += count
#     print(count,sum)
#
# str1 = "milk"
#
# # i = 0
# # while i < len(str1):
# #     print(str1[i])
# #     i = i + 1
#
# i = 0
# while i < len(str1):
#     print(str1[i:])
#     i = i + 1

#

# i = 0
# result = 0
#
#     print(i, result)
#     i = i + 1
# while i < 10:
#     result = 1 * 2

# import random
# i = 0
# secret = 0
# j = 1000
# while i < 10:
#     secret = random.randint(1, 1000)
#     print("случайное число ", secret, "под номером: ", i)
# if secret > j:
#     j = secret
#     print(j)
#     i += 1
# print("максимальное число:", j)


# years = 5
# money = int(input())
# percentage = 10
#
# i = 0
# while i < years and money > 0:
#     i += 1
#     money = money + (money * percentage / 100)
#     print(money)

# i = 0
# while i < 1000000:
#     i += 1
#     print(i)

# list1 = ["Vova",2004, "M","18",['harry','das','asda']]
#
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

#
# list1 = ["Begimai", "Johny", "Fred", "Obama", "Trump", "Cat", "Boris", "Steven"]
# criminal = input("Enter criminal's name: ")
#
# i = 0
# while i < len(list1):
#     if criminal in list1[i]:
#         if criminal == list1[i]:
#             print("Адрес криминала:", i)
#         else:
#             print("не найден")
#         break
#     i += 1


# data = ['Wt', 'Ht', 342432423424324, 5.996, 5.77778,
#         'Insurance_History_2', 34243242342432124545312312534534534, 'Insurance_History_4',
#         'Insurance_History_5', 'Insurance_History_7', 234242049004328402384023849028402348203,
#         55, 66, 11, 'Medical_Keyword_3',
#         'Medical_Keyword_4', 'Medical_Keyword_5', 'Medical_Keyword_6', 34243242342432124545312312534534534534503495345,
#         'lalalalallalalalalalalalalalalala', 23409284028430928420483209482904380428, 'Medical_Keyword_10',
#         'Medical_Keyword_11',
#         92384923849023849023842903482934324290, 93429423018319238192004829423482942, 'Medical_Keyword_14',
#         'Medical_Keyword_15',
#         'Medical_Keyword_16', 5.888, 'Medical_Keyword_18asfdasfdasfdasfdasdfasdfas', 'Medicagsfgsfgsfkgjsfkg',
#         9.131, 0.978, 'Famidasdasdlasdlaspdlaspdlasp2948203948',
#         'Familygsdglksflg2849023840923;fksdkgsd234234234238409238490238', 'Family_Hist_4',
#         'Family_Hist_5', 9.19, 'Medical_History_2', 'Medical_History_3', 'Medical_History_4',
#         13, 'Medical_History_6', 'Medical_History_7', 111, 'Medical_History_9',
#         123.7773, 'Medical_History_41', 55823428882482374824828472348, 'Product_Info_3', 1111111111111111111111,
#         'Product_Info_5', ]
#
# #
# # if isinstance(data[3], float):
# #     if data[3] % 1 >= 0.8:
# #         data[3] = round(data[3])
# #         print(data[3])
#
#
#
#
# i = 0
# while i < len(data):
#     obj = data[i]
#     if isinstance(obj, float):
#         if obj % 1 >= 0.8 or obj % 1 <= 0.2:
#             data[i] = round(obj)
#         else:
#             data[i] = int(obj)
#
#     elif isinstance(obj, int):
#
#         if len(str(obj)) >= 20:
#             del data[i]
#             i -= 1
#
#     elif isinstance(obj, str):
#         if len(obj) > 50:
#             del data[i]
#             i -= 1
#     i += 1
# print(data)

