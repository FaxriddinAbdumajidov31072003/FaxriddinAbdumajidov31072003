'''def hello():
    print("Hello world")

def karra(a):
    print(a*2)'''

'''def kopaytiruv(*args):
    natija=1
    for i in args:
        natija*=i
    return natija
print(kopaytiruv(2,3,4))'''


# 1 - masala 
'''def almashtirish(a):
    if len(a)%2:

       
    return yakun          #chala tugatw kere
b = [1,2,3,4,5,6,7,8]
print(almashtirish(b))'''




'''def almashtirish(a):
    return a[len(a)//2:]+a[:len(a)//2]
b = [1,2,3,4,5,6,7,8]
print(almashtirish(b))'''

'''def almashtirish(a):
    if len(a)%2:
        yakun = a[(len(a)//2)+1:]
        yakun.append(a[len(a)//2])
        yakun+= a[:len(a//2)]
    else:
        yakun = a[len(a)//2:]+a[:len(a)//2]
       


    return yakun
b = [1,2,3,4,5,6,7,8,9]
print(almashtirish(b))'''


'''def ciqar(son):
    if son==0:
        return 0
    ciqar(son//10)
    print(son%10, end=" ")

ciqar(123)'''



'''def ciqar(a):
    if a==0:
        return 0
    ciqar(a-1)
    print(a,end=" ")
ciqar(6)'''

'''def ciqar(a):
    if a==0:
        return 0
    ciqar(a-1)
    return a*a
    
print(ciqar(5))'''



'''from a import *
print(qoshish(2,3))
print(ayirish(3,3))
print(bolish(9,3))
print(kopaytiruv(2,3))'''








  













