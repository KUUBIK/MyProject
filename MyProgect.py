from matplotlib import pyplot as plt
import random


my_list = ['bacon',"beef","chicken","cookedmeat","duck","ham","kidneys","lamb","liver","mince","pate",
           "salami","sausages","pork","pork_pie","sausage_roll","turkey","veal", "apple", "juise"]
# help = []
# for i in range(0, 10):
#     i = my_list[i]
#
#
#     my_data = {i:['кол-во:',random.randint(100, 300), 'цена', random.randint(400, 5000), 'день или месяц']}
#     help.append(my_data)
#     print(my_data)
# print(help)


u = 0
kol = []
price = []
key = []
name = []
while u < 15:
    i = my_list[u]
    global my_data
    my_data = {i:{'кол-во':random.randint(10, 300)  , 'цена': random.randint(200, 2000), 'месяц':"januar"}}

    print(my_data)
    global a
# Алгоритм для подсчета кол-во проданного за месяц
    a = my_data.get(my_list[u])
    key = my_data.keys()
    b = a.setdefault('цена')
    a = a.setdefault('кол-во')

    xy = [a] + [i] + [b]
    kol.append(xy)
    print(xy)
    u = u + 1
# price.sort()
kol.sort()
print(kol)
# print("Общее кол-во проданного товара:" + str(sum(kol)) + " Единиц")
print("Больше всего было проданно:" + str(max(kol)[0]) + " Единиц " + str(max(kol)[1]) )
print("Меньше всего было проданно:" + str(min(kol)) + " Единиц")



# create a line chart, years on x-axis, gdp on y-axis
# plt.plot(price, kol, color='green', marker='o', linestyle='solid')
#
# # add a title
# plt.title("Продажи за сентябрь-ноябрь")
#
# # add a label to the y-axis
# plt.savefig('myfig.png')



