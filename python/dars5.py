import os
from random import randint
os.system('cls')
"""
'''list1 = [(1,9,0),(2,0,4),(1,0,3),(4,4), (5,0,1)]
list2 = []
natija = []
for i in list1:
    list2.append(i[1])
list2.sort()
for i in list2:
    for j in list1:
        if i==j[1]:
            natija.append(j)
            list1.remove(j)
            break

print(natija)'''

'''list1 = [(1,0,3),(1,9,0),(2,0,4),(4,4), (5,0,1)]    HATORO ISHLIDI
list2 = []
natija = []
for i in list1:
    list2.append(i[1])
list2 = sorted(list(set(list2)))
print(list1)
for i in list2:
    for j in list1:
        print(i, j)
        if i==j[1]:
            natija.append(j)
            list1.remove(j)
            print(list1)

print(natija)'''


'''st1 = {'Apple', 'Google', 'Amazon', 'Google'}
st2 = {'Uber', 'Meta', 'Microsoft', 'Google', 'Apple'}
print(st1)
print(st2)
print(st1.intersection(st2))'''

'''lt1 = [1,2,3,3,4,5]
lt2 = [5,1,0,3]
lt3 = [9,9,9,3]
# print(st1.intersection(st2))
print(set(lt1).intersection(lt2, set(lt3)))'''


'''st1 = {'Apple', 'Google', 'Amazon', 'Google'}
st2 = {'Uber', 'Meta', 'Microsoft', 'Google', 'Apple'}
print(st1)
print(st2)
print(st1.difference(st2))
print(st2.difference(st1))'''

'''st1 = {'Apple', 'Google', 'Amazon', 'Google'}
st2 = {'Uber', 'Meta', 'Microsoft', 'Google', 'Apple'}
print(st1)
print(st2)
st2.difference_update(st1)
print(st1)
print(st2)'''

'''st1 = {'Apple', 'Google', 'Amazon', 'Google'}
st2 = {'Uber', 'Meta', 'Microsoft', 'Google', 'Apple'}
print(st1)
print(st2)
st3 = st1.union(st2)'''


'''st3 = { 'apple','Microsoft','sms'}
st3.pop()
print(st3)
st3.discard('Microsoft')
print(st3)'''


'''key -> kalit
value -> qiymat'''


'''spark = {}
spark = dict()
spark = {
    'narxi':8700,
    'yili':2020,
    'rangi':'oq',
    'razmeri': [25,21,12]
}'''

'''dct = {
    'model':'Porsche',
    'max speed': 360
}

print(dct['model'], dct['max speed'])'''
# print(dct['color']) -> hatoli beradi

'''dct2 = {
    'max speed' : 360
}
dct2[color] = 'white'
dct2['max speed'] = 200
print(dct2)

print(a := 9)'''
"""

'''dct = {}
for i in range(3):
    key = input('key kiriting:')
    dct[key] = input()

print(dct)'''


'''l1 = [1,1,1,1,1,2,3,4,5,2,4,5,8]
for i in set(l1):
    print(f"{i} -> {l1.count(i)}")'''

'''l1 = [1,1,1,1,1,2,3,4,5,2,4,5,8]
dct = dict()
for i in set(l1):
    dct[i] = l1.count(i)
print(dct)'''


u1 = {
    'name' : 'Eshmat',
    'age'  : 24,
    'phones': {
        'phone1':{
            'kompaniya':'ucell',
            'tarifi':'beshqozon',
            'raqami':12356
        },
        'phone2':{
            'kompaniya':'beeline',
            'tarifi':'toshqozon',
            'raqami':65321
        }
    }
}

# print(u1['phones']['phone1'])
'''list1 = u1.keys()
print(list1)
print(*u1)'''

# print(u1.values())
'''for i in u1.values():
    print(i)'''

'''for i in u1.keys():
    print(i)'''

'''for key, value in u1.items():
    print(key, value)'''

# print(u1.get('kimdur'))


'''a = list()
for i in range(20):
    a.append(randint(5,10))
print(a)'''

'''a = [randint(20,25) for i in range(100)]
print(a)'''

'''sabr = {
    1: 258,
    2: 250,
    3: 10,
    'salom': 956,
    5:253
}
list1=[]
for i in sabr.values():
    list1.append(i)
list1 = sorted(list1, reverse=True)

for i in range(3):
    for key, value in sabr.items():
        if list1[i]==value:
            print(key)'''


sabr = {
    1: 258,
    2: 250,
    3: 10,
    'salom': 956,
    5:253
}

for i in range(3):
    print(max(sabr, key=sabr.get))
    sabr.pop(max(sabr, key=sabr.get))