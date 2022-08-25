'''lt1 = [1,1,1,1,12,3,4,5]
lt2 = set(lt1)
for i in lt2:
    count = lt1.count(i)
    print(i, "shuncha bor", count)'''

'''lt1 = [1,1,1,1,2,23,23,4,5]
for i in set(lt1):
    print(f"{i}->{lt1.count(i)}")'''


'''lt1 = [1,1,1,1,2,23,23,4,5]
dct = dict()
for i in set(lt1):
    dct[i] = lt1.count(i)
    print(dct)'''


from multiprocessing.sharedctypes import Value
from random import randint

from cv2 import sort

    #(   #1    )   (     #2        )   (   #3    )
'''a = [randint(5,10) for i in range(20)  if i%2==0]
print(a)'''

# 1 - masala
'''a = [randint(20,25) for i in range(100) ]
dct = dict()
for i in set(a):
    #dct[i] = a.count(i)
#print(dct)
    print(f"{i} -> {a.count(i)}%")'''

#2 - masala
'''n = int(input())
dct = dict()
for i in range(1,n+1):
    dct[i]= i*i
print(dct)'''


# 3 - masala
'''a ={1:256,
    2:20,
    3:400,
    4:30,
    5:600}
dct = dict()
b = list(a.values())
b.sort(reverse=True)
for key, value in a.items():
    for i in range(3):
        if b[i]==value:
            print(key)'''

# 4 - masala 
'''d1 = {'a':100,
      'b':200,
      'c':300
      },
d2 = {'a':300,
      'b':200,
      'd':400
      },
d3 = {'a':400,
      'b':400,
      'c':400
      }
dct = dict()'''


'''dict1 = {2:10, 3:5, 4:7, 8:6}
natija = {}
b = dict1.values()
b = list(b)
b.sort()
for i in b:
    for key, value in dict1.items():
        if i==value:
            natija[key] = Value
            break

dict1 = natija
print(dict1)'''












              
    

   



   
        





    


         

