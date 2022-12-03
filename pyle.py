# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
"""
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")


lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.




def mult_lst(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    print(new_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)
"""
# DZ_4
# # 4_1. Вычислить число Пи c заданной точностью d
# import math

# d = int(input("задайте точность числа π,чисел после запятой : "))

# if d < 1 or d > 10:
#     print("точность выходит за границы диапазона")
# else:
#     p = str(math.pi)
#     print(p[0 : (d + 2)])
#  4_2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"{lst}")
# 4_3.Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

#  ranfromdom import randint

# N = int(input("Введите число : "))
# mass = []

# for i in range(N):
#     mass.append(randint(0, N))
# print(mass)
# mass2 = []
# for i in mass:
#     if mass.count(i) == 1:
#         mass2.append(i)
# print(mass2)
# 4_4. Задана натуральная степень k. Сформировать случайным
#  образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# from random import randint
# import itertools

# k = randint(2, 3)


# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def get_polynomial(k, ratios):
#     var = ["*x^"] * (k - 1) + ["*x"]
#     polynomial = [
#         [a, b, c]
#         for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue="")
#         if a != 0
#     ]
#     for x in polynomial:
#         x.append(" + ")
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = " = 0"
#     return "".join(map(str, polynomial)).replace(" 1*x", " x")


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open("33_Polynomial.txt", "w") as data:
#     data.write(polynom1)


# 4_5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# import re
# import itertools

# file1 = "33_Polynomial.txt"
# file2 = "33_Polynomial2.txt"
# file_sum = "34_Sum_polynomials.txt"


# def read_pol(file):
#     with open(str(file), "r") as data:
#         pol = data.read()
#     return pol


# def convert_pol(pol):
#     pol = pol.replace("= 0", "")
#     pol = re.sub("[*|^| ]", " ", pol).split("+")
#     pol = [char.split(" ") for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == "x":
#             i.insert(0, 1)
#         if i[-1] == "x":
#             i.append(1)
#         if len(i) == 1:
#             i.append(0)
#     pol = [tuple(int(x) for x in j if x != "x") for j in pol]
#     return pol


# def fold_pols(pol1, pol2):
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key=lambda r: r[1], reverse=True)
#     return res


# def get_sum_pol(pol):
#     var = ["*x^"] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == "0":
#             del x[0]
#         if x[-1] == "0":
#             del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == "1" and x[1] == "*x^":
#             del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == "1":
#             del x[-1]
#             x[-1] = "*x"
#         x.append(" + ")
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = " = 0"
#     return "".join(map(str, new_pol))


# def write_to_file(file, pol):
#     with open(file, "w") as data:
#         data.write(pol)


# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)
