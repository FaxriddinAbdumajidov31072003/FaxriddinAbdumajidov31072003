'''li = ["kim", "hayr", "arsenal"]
natija = ''

for index, i in enumerate(li):
    natija = natija.join(sorted(i))
    print(natija)
    li[index] = natija
    natija = ''

print(li)'''



'''l = [2,0,1,4,5,8,7]
# l.sort()
k = sorted(l)
print(k)'''

'''a = [2,3,1,4,5,6]
print(a[-1])'''

'''a = [2,3,1,4,5]
print("reversdan oldin", a[0])
a.reverse()
print("reversdan keyin", a[0])
print(a)'''


'''a = [1,2,4,5,3]
a.reverse()
# kitob = a[:]
kitob = a.copy()
a.reverse()
print("a=", a)
print("kitob=", kitob)'''

'''a = [1,3,5,4,2]
print(sorted(a, reverse=True))
print(a)'''


'''l = [2,1,4, 'salom', 4]
l.remove(4)
son = l.pop(2)
print(son)
print(l)
del l
print(l)'''

"""l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10, 'kimdur']
'''for i in l2:
    l1.append(i)'''
l1.extend(l2)
print(l1)"""

'''l1 = [2,3]
l1.extend("salom")
print(l1)'''

'''l1 = [2,3,4,3,3,3,1,2,2]

for i in l1:
    if l1.count(i)>1:
        print(i)
        for j in range(l1.count(i)):
            l1.remove(i)
            print(l1)'''


'''l1 = [2,3,4,3,3,3,1,2,2]
l2 = []

for i in l1:
    if l1.count(i)>1 and i not in l2:
        l2.append(i)
        print(i)'''



'''l1 = [2,3,9,5,0,6,7]
min = l1[0]
max = l1[0]
sum = 0
for i in l1:
    sum+=i
    if min>i:
        min=i
    if max<i:
        max=i

print(f"min = %d | max = %d | sum = %d" %(min, max, sum))'''

'''l1 = [2,3,9,5,0,6,7]
l1.sort()
sum = 0
for i in l1:
    sum+=i
print(f"min = %d | max = %d | sum = %d" %(l1[0], l1[-1], sum))'''



'''l1 = [2,3,9,5,6,7]
print(f"min = %d | max = %d | sum = %d" %(min(l1), max(l1), sum(l1)))

print(min("salom"))
print(max("salom"))'''

# print(min(5)) # hatoli beradi chunki int iterable emas


# tuple
'''- indekslangan
- (), tuple()
- tartiblangan'''

'''turp = (2,1,3)
print(type(turp))
print(turp[0])
turp = list(turp)
print(type(turp))
turp[0] = 52
print(turp)
turp=tuple(turp)
print(type(turp))
print(turp)

print(turp.count(52))
print(turp.index(52))


print("salom".index('lom'))'''




'''turp = (2,1,0,45,32)
turp = list(turp)
turp.sort()
turp = tuple(turp)
print(turp)'''


'''turp = (2,1,0,45,32)
turp = tuple(sorted(turp))
print(turp)'''


'''turp = (2,1,0,45,32)
print(sorted(turp))
print(len(turp))'''


'''li = [(1,4,3), (3,2), (2,0,1), (1,4,2)] # -> li[(2,0,1),(3,2),(1,4,3),(1,4,2)]

for i, malumot in enumerate(li):
    print(f"i={i} | malumot = {malumot}")
    li[i] = tuple(sorted(malumot))
print(li)'''

'''turp = (3,2,4,5)
for i, malumot in enumerate(turp):
    print(f"i={i} | malumot = {malumot}")'''

# set

a = {"samsung","IBM", "apple"}
print(type(a))
print(a)
a.add("kitob")
print(a)
a.pop()
print(a)


'''a = [1,2,3,4,5]
a.pop()
print(a)'''

a = [1,2,3]
b = [2,3,4]
c = a+b
print(c)

