#a = lambda x: x+15
#print(a(4))

#a = lambda x=12: x+15
#print(a())


#a = lambda b,c,x: b+c+x
#print(a(2,3,4))

# from curses.ascii import isupper
# from re import X


#from turtle import color


#def func(n):
 #   return lambda x: x**n

#a = func(2) # daraja
#print(a(4)) # asos


#map(function,variables)

#def sum(a,b):
 #   return a+b

'''x = list(map(sum,"3","4"))
print(x)'''

'''a = list(input().split())
print(a)'''

'''l1 = [1,2,3,4]
l2 = [2,3,4,5,6,7]

x= list(map(lambda x,y: x+y, l1,l2))
print(x)'''


'''l = ['arsenal','kim','kitob']
natija = list(map(list,l))
print(natija)'''

'''list1 = [1,2,3,4,5,6,7]
x = list()
x = list(filter(lambda x: x%2!=0,list1))
print(x)'''

'''l1 = ['kim',5,'nima',6,'qachon',7]
natija = list(filter(lambda x: type(x)==str,l1))
print(natija)'''

'''l1 = [1,-2,3,6,-5]
a = list(filter(lambda x: x<0 , l1))
print(a)'''


'''a = input("ma'lumot kiriting: ")
try:
    print(a+4)
except :
    print("amalni bajarib bolmaydi")'''

'''a = input("Malumot kiriting: ")
try:
    print(a*bd)
except:
    print("amalni bajarib bolmaydi")'''



################## F A Y L ###################


'''f = open("f1.txt",'w')
for i in range(1,10) :
    for j in range(1,6):
        f.write(f"{j}*{i}={i*j}")
        if i*j<10:
            f.write("    ")
        else:
            f.write("   ")
    f.write("\n")
f.write("\n")
for i in range(1,10) :
    for j in range(6,11):
        f.write(f"{j}*{i}={i*j}")
        if i*j<10:
            f.write("    ")
        else:
            f.write("   ")
    f.write("\n")
f.close()'''

'''f = open("f1.txt",'r')
a = f.readlines()
print(a)
for i in a:
    for j in i.split():
        if len(j)==5:
            print(j)'''


'''f = open("f1.txt", 'r')
f1 = open("k.txt",'w')
f2 = open("a.txt",'w')

a = f.readlines()
for i in a:
    for j in i.split():
        if 'a' in j:
            f2.write(j+"\n")
        if 'k' in j:
            f1.write(j+"\n")
f.close()       
f1.close()
f2.close()'''


'''f = open("f1.txt", 'r')
a = f.readlines()
b = 0
for i in a:
    print(i)
    for j in i.split():
        if j[0].isupper():
            b+=1
print(b)
f.close()'''

'''f = open("f1.txt", 'r')
f1 = open("c.txt",'w')
a = f.readlines()
for i in a:
    for j in i.split():
        if len(j)<5:
             f1.write(j+" ")
f.close()
f1.close()'''

'''f = open("f1.txt", 'r')
f1 = open("juft.txt",'w')
f2 = open("toq.txt",'w')
a = f.readlines()
for i in a:
    for j in i.split():
        if int(j)%2==0:
            f1.write(j+" ")
        else:
            f2.write(j+" ")
f.close()
f1.close()
f2.close()'''


'''with open("f1.txt",'r') as f:
    a = f.read()           #ikkinchi elon qiliw usuli
    print(a)'''

#with open("f1.txt", encoding='utf-8') as f:   agar hatolik bersa wuni yoziw kere


'''with open("f1.txt",'r') as f:
    for i in f.read().split():
        print(i)'''

      #/////////////////////////////////////////

'''import os
os.system("cls")
f = open("nimadur.txt",encoding='utf-8')
a = f.readlines()
soz = {}
for i in a:
    nimadur = []
    i = i.split(",")
    if '"' in i[1]:
        x = i[2]
    else:
        x = i[1]
    for j in a:
        j = j.split(",")
        if '"' in j[1]:
            q = j[0]+","+j[1]
        else:
            q = j[0]
        if x in j:      
            nimadur.append(q)
    soz[x] = nimadur
for k,v in soz.items():
    print(f"\n\n{k}:\n {v}")
print("""
1. Xamma keylar
2. Xamma valuelar
""")
number = int(input("Raqam kiritin: "))
if number == 1:
    i = 0
    for k in soz.keys():
        i += 1
        print(f"{i}.{k}")
elif number == 2:
    for value in soz.values():
        print(f"\n\n{value}")
f.close()'''
      
        
                   

           














