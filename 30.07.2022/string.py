#x = len("salom")
#print(x)

'''f = "salom"
x = len(f)
'''

#x = input("gap kiriting: ")
#print(x[len(x)//2:]+x[:len(x)//2])


'''txt = "I hate programming. I hate foundation 57"
qidiruv = input("Soz kiriting: ")
x = txt.find(qidiruv)
if(x==-1):
    print("error")
else:
    print(x,"- indexdan boshlangan")'''


'''txt = "I hate homework. I hate programming. I hate foundation 57 "
qidiruv = input("Soz kiriting: ")
x = txt.find(qidiruv)

if qidiruv==-1 :
    print("error")
else:
    #print(qidiruv[::-1]*(x+1))
    print((qidiruv[::-1]+" ")*x)'''#necinci indexda turgan bolsa shuncha marta chiqaradi


'''txt = "I hate homework. I hate programming"
eski = input("qaysi sizni ozgartirasiz: ")
yengi = input("yangi soz kiriting: ")
txt = txt.replace(eski, yengi,1)  #aynan qaysini ozgartirish kerakligini korsatadi
txt = txt.replace(eski, yengi)  #ozgarishi kerak bolgan soz nechta bolsa hamasini ozgartiradi
print(txt)'''


'''n = int(input())
for i in range(1,n+1,1):
    print("i=",i,"->",end=' ')   # uch burchak
    for j in range(1,i):
        print(j,end=' ')
    print()'''


'''n = int(input())
juft = 0
toq = 0
for i in range(1,n+1,1):
    if i%2==0:
        juft+=i
    else:
        toq+=i
print(f"juft sonlar->{juft}")
print(f"toq sonlar->{toq}")'''


'''n = input("soz kiriting: ")
unli = 0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        
        unli+=1
print(f"unli={unli}")'''

'''txt = "salom foundation"
n = "aoiue"
count = 0
for i in txt:
    if i in n:
        count+=1
print(count)'''





