from matplotlib import pyplot as plt
import random


my_list = ["chocolate","juise","Meat","fruit", "alcohol", "bakery products"]
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
my_sum = []
while u < 6:
    i = my_list[u]
    global my_data
    my_data = {i:{'кол-во':random.randint(10, 400)  , 'цена': random.randint(200, 2000), 'месяц':"januar"}}

    # print(my_data)
    global a
# Алгоритм для подсчета кол-во проданного за месяц
    a = my_data.get(my_list[u])
    key = my_data.keys()
    b = a.setdefault('цена')
    a = a.setdefault('кол-во')

    xy = [a] + [i]
    xz = a * b
    kol.append(xy)
    name.append(a)
    price.append(b)
    my_sum.append(xz)
    print(xy)
    print(b)
    print(my_sum)
    u = u + 1
price.sort()
print(price)
name.sort()
print(name)
print(my_sum)

kol.sort()
print(kol)



number1 = "Общее кол-во проданного товара:" + str(sum(name)) + " Единиц"
number2 = "Больше всего было проданно:" + str(max(kol)[0]) + " Единиц " +  str(max(kol)[1])
number3 = "Меньше всего было проданно:" + str(min(kol)[0]) + " Единиц " +  str(min(kol)[1])
number4 = "Общая цена проданного: " + str(sum(my_sum))


new_Kol = []
name_kol = []
for i in range(0,6):
    new = kol[i][0]
    new_name = kol[i][1]
    new_Kol.append(new)
    name_kol.append(new_name)
print(new_Kol)
print(name_kol)





# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(name_kol)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, new_Kol)
plt.ylabel("Кол-во проданного",  fontsize=15)
plt.title("Продажи за июнь-август",  fontsize=15)

plt.xlabel(number1 + "\n" + number2 + "\n" + number3 + "\n" + number4 + "\n", fontsize=15, ha = 'left')


# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(name_kol)], name_kol,  fontsize=15, color = "green")

plt.show()
