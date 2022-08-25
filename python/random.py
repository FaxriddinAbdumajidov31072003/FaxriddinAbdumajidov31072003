import random
lowers = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '0123456789'
uppers = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '[]{}()*;/,._-'

all = lowers + uppers + numbers + symbols
length = 16
password ="".join(random.sample(all,length))
print(password)