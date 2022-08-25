
# print("Hello World")

'''
Kop qatorli komentariya
'''

"""
Ko'p qatorli komentariya 2-usuli
"""

#print('O\'zbekistan, g\'oz')
#print("O'zbekiston")

#print('Men "BMW"\n sotib oldim')
#print("Men 'BMW' sotib oldim")

'''print("""Men Eshmat Toshmatov
1568-yil DC da tavallud topgan
kimdurlar nimadurlar""")'''

#print("salom","dunyo")

# a = 5
# b = 2
# print(a,b)


'''print(a+b) #7
print(a-b) #3
print(a/b) #2.5
print(a//b)#2
print(a%b) #1 qoldiqni yaxlitlab beradi
print(a*b) #10
print(b**a)# 2 ning 5 chi darajasi 2^5  **->darajani hisoblaydi
'''

#primitive typlar -> (float, bool, int, str)
#none primitive typlar -> 



'''ism = "Eshmat"
yosh = 26
print(ism, yosh, end=" ")
print(yosh)'''

'''ism_familya = "Fara"
ism_familya = ism_familya + " Eshmatov" + " 17 yosh"
print(ism_familya)'''
'''son = 25
son2 = 24
son3 = int(str(son)+str(son2))
print(str(son+son2)+"salom")'''


'''ism = "eshmat"
familiya = "toshmatov"
ism_familiya = f"{ism} {familiya}"
print(ism_familiya)

son = 24
son2 = 25
naitja = int(f"{son}{son2}")
print(naitja)'''

ism = "John" #nohj
familiya = "Doe"
yosh = 36
#print(ism,familiya,yosh)
#printf("Ism:%s\n Familiya:%s\n Yosh:%d", ism, familiya, yosh)
#print("Ism:",ism,"\n","Familiya:",familiya,"\n","Yosh:", yosh)
#print(f"Ism: {ism}\nFamilya: {familiya}\nYosh: {yosh}")
print(f"""{ism} was born in USA.
His second name is {familiya} and he is {yosh+3} years old!
Got it man?""")

# print(ism[1])

'''a = 23
b = 20
a,b = b,a
print(a,b)'''

'''ism, familiya = "Kevin", "McAlester"
print(ism, familiya)
a,b,c,d,e,f,g = 1,2,3,4,5,6,7'''

#printf("Son kiriting: ");
#scanf("%d", &son);
# 1-usuli
'''print("Son kiriting:", end=' ')
son = input()'''
# 2-usuli
'''son = int(input("Son kiriting: "))
son2 = int(input("Son2 ni kiriting: "))
print(son+son2)'''

# 1-usul
#soz = "salom"
#soz = soz.upper()
#print(soz)

# 2-usul
#soz = "salom".upper()
#print(soz)

# 1-usul
# soz = "SAlom"
# soz = soz.lower()
# print(soz)

# 2-usul
# soz = "salom".lower()
# print(soz)

# 3-usuli faqat o'zlashtirmaydi
# soz = "SAlom"
# print(soz.lower())

# title() barcha so'zlarning bosh harifini kattaga o'zgartiradi
# soz = "john doe Kim nega book. Nimadur. arsenal"
# soz = soz.title()
# print(soz)

# capitalize() birinchi so'zni birinchi harfini kattaga o'zgartiradi
soz = "kim nima desa desinu. uyog'ini bilmiman";
soz = soz.capitalize()
print(soz)