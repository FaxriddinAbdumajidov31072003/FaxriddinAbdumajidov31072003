'''print("salom"[::-1])
print("salom"[3])
print("salom"[2:])

print("salom"[1:3]) # al chiqadi
print("salom"[0:4:2])
print("salom"[::2])

[start:stop:step]'''

'''x = input("Gap kiriting: ")
print(x[(len(x)//2):] + x[:len(x)//2])'''

'''x = input("Gap kiriting: ")
print(x[:(len(x)//2)-1:-1] + x[:len(x)//2])'''

'''gap = "Pythonga salomxushshsh kelibsiz. Dars qiling xush"
natija = "xush" in gap
print(natija)
print(type(natija))
print("gap",type(gap))'''

'''natija = bool(23+3)
print(natija)'''



'''txt = "I hate programming. I hate foundation"
x = txt.count("hate foundation")
print(x)'''


'''txt = "I hate programming. I hate foundation"
qidiruv = input("So'z kirit: ")
x = txt.find(qidiruv)
if(x==-1):
    print("siz qidirgan so'z mavjud emas")
else:
    print(x,"- indexdan boshlanga")'''


'''txt = "Foundation kim arsenal nimadur"
qidiruv = input("string ichidagi so'zni top: ")
turgan_joyi = txt.find(qidiruv)
if(turgan_joyi==-1):
    print("topomadin")
else:
    print((qidiruv[::-1]+" ")*turgan_joyi)'''


'''txt = "I hate programming. I hate foundation"
qidiruv = input("So'z kirit: ")
turgan_joy = txt.index(qidiruv)
print(turgan_joy)'''


'''txt = "I hate programming. I hate foundation"
eski = input("Qaysi so'zni o'zgartirasiz: ")
yengi = input("Yangi so'z kiriting: ")
txt = txt.replace(eski, yengi)
print(txt)'''


'''txt = "I hate programming. I hate foundation"
eski = input("Qaysi so'zni o'zgartirasiz: ")
yengi = input("Yangi so'z kiriting: ")
txt = txt.replace(eski, yengi)
txt = txt.replace(yengi, yengi,1)
print(txt)'''


'''txt = "I hate programming. I hate foundation"
natija = txt.split(' ')
print(natija[2][::-1])
#print(natija[2][::-1])'''


'''i = list(range(,10,1)) -> xatoli beradi
i = list(range(0,10,1))
i = list(range(0,10))
i = list(range(10)) #-> bitta son kiritilinsa start default 0 ni step default 1 ni anglatadi
print(i)'''

'''n = int(input())
for i in range(1,n+1,1):
    print("i=",i,"->",end=' ')
    for j in range(1,i):
        print(j, end=' ')
    print()'''

# yuqoridagi kodni C dasturlash tilidagi ko'rinishi
'''for(int i=1; i<n+1; i++){
    printf("i=%d->", i)
    for(int j=1; j<i; j++){
        printf("%d ", j);
    }
    puts("");
}'''


'''toq=0
juft=0
n = int(input("nechigacha:\n>>> "))
for i in range(n):
    if i%2:
        toq+=i
    else:
        juft+=i

print(f"toq={toq}\njuft={juft}")'''



'''for(int i=0; i<strlen(txt); i++){
    printf("%c ", txt[i])
}'''


'''txt = "salom foundation"
for i in txt:
    print(i, end=' ')'''


'''txt = input("Gap kiriting: ")
count=0
for i in txt:
    if i not in "aeuioAEUIO": # ushbu string ichida mavjud bo'lmagan holda true qaytaradi
        count+=1
        # break
        # continue
        # pass
print(count)'''


'''txt = input("Gap kiriting: ")
count=0
for i in txt:
    if i in "aeuioAEUIO": # ushbu string ichida mavjud bo'lgan holda true qaytaradi
        count+=1
print(count)'''



'''a = ['toshkent', 'samarqand', 'buxoro', 'xiva', 'xorazm', 1991, 12, True, [1,2,[5,[10,2]]]]
# a = list()
print(a)
print(a[2])
print(a[2][5])
print(str(a[6])[0])
print(a[8][2][1][0])'''

'''l = [1,False, 45, 'salom', [1,2]]
for i in l:
    print(i, type(i))'''


'''l = [1,False, 45, 'salom', [1,2]]
for i in l:
    if type(i) == list:
        for j in i:
            print(j)'''


'''l = ['salom',25]
l.append(12)
l.append('arsenal')
print(l)'''
    
'''l = ["salom",1,2,3]
l.insert(1,'kim')
print(l)'''


'''l = ["salom",1,2,3]
l.clear()
print(l)
l.append('kurs')
print(l)'''

'''l = [1,2,3,4,5,'salom','salom']
l.remove('salom')
print(l)'''
















