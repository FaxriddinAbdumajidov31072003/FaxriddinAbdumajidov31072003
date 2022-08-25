# def hello():
#     print("Hello world")

# def karra(a):
#     print(a*2)

# dict = {1:2, 3:4, 5:6}
# hello()
# karra("salom")
# karra(2)
# karra([1,2,3,4])
# karra((1,2,3,4))
# karra(True)
# karra(dict) -> hatoli beradi


# a = [4,3,2.2,45, False]
# a.sort()
# print(a)

# def qoshish(a, b):
#     '''BU function a va b gakelgan qiymatlarni o'zaro qo'shib qaytaradi'''
#     return a+b

# def ayirish(a: int,  b: int) -> int:
#     return a-b



# a = qoshish(2,4)
# b = ayirish(3.5, 2.2)
# print(a:=qoshish(5,6))
# print(f"%.2f" %b)
# print(3.50-2.20)


# def daraja(asos: int=2, daraja: int=2) ->int:
#     return asos**daraja

# def daraja(asos=2, daraja=2) ->int:
#     return asos**daraja
# print(daraja(3))

# argumets -> args
# def kopaytiruv(*args):
#     print(args)
    
# a = (2,3,1,4,56,6)
# print(kopaytiruv(*a, *[2,3,4,5], *"salom"))

# def kop(*args):
#     natija = 1
#     for i in args:
#         natija*=i
#         print(natija)
#     return natija
# a = (2,3,1,4,56,6)
# print(kop(*a, *[2,3,4,5], *"salom"))

# **kwargs
# key word arguments


# def dict_bilan_ishlash(a):
#     print(a)

# def dict_bilan_ishlash2(**kwargs):
#     print(kwargs)

# dict1 = {3:2, '3':5}
# dict_bilan_ishlash(dict1)
# st = 8
# dict_bilan_ishlash2(foundation=st, students=13, boxodr=1, st=st)


# a = [1,2,3,4,5]
# print(a[:len(a)//2])



# def natija(list1):
#     yakun = list()
#     if len(list1)%2:
#         yakun+=list1[1:len(list1)//2]
#         yakun.append(list1[0])
#         yakun.append(list1[len(list1)//2])
#         yakun.append(list1[-1])
#         yakun+=list1[(len(list1)//2)+1:len(list1)-1]
#     else:
#         yakun+=list1[1:len(list1)//2]
#         yakun.append(list1[0])
#         yakun.append(list1[-1])
#         yakun+=list1[len(list1)//2:len(list1)-1]
#     return yakun

# a = [1,2,3,4,5,6,7,8,9]
# print(natija(a))

# a = 34

# def natija(a):
#     a+=3
#     return a

# def natija2():
#     global a
#     a+=3
#     return a

# print(f"funksiyadan so'ng : {natija(a)}")
# print(f"shunchaki print: {a}")
# print(f"global ishlatilgan funksiyadan so'ng so'ng : {natija2()}")
# print(f"shunchaki print: {a}")


def rec_sum(son):
    if son==0:
        return 0
    return son%10+rec_sum(son//10)

print(rec_sum(563))




# a = {1:2, 3:4, 5:6}
# b = {4:5, 5:6}
# a.pop(3)
# print(a)
# a.popitem()
# print(a)
# a.update(b)
# print(a)
# a.update([{'salom',2}, ('llll','kimdur'),['asdf',[1,2,3,4]]])
# print(a)



# import math
# import os
# import random



# import matplotlib
# import colorama



# Built-in libraries
# third party libraries
# user defined libraries



# import functions

# print(functions.nimadur())
# a = functions.sum(4,5)
# print(a)

# from functions import sum
# print(sum(2,4))

from functions import sum as s
print(s(2,4))

# from functions import *
# sum()
# nimadur()
