import os

os.system('cls')

'''class Employee:
    oylikni_oshir = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'_'+last+'#gmail.com' 

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.oylikni_oshir)

    def get_info(self):
        return f"{self.full_name()} ning oyligi {self.pay}"

class Developer(Employee):

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        #print(self.get_info())

    def get_info(self):
        return super().get_info()+f" .{self.full_name()} {self.prog_lang} dasturchisi"

class Manager(Employee):
    def __init__(self,first,last,pay, employees = None):
       super().__init__(first,last,pay)
       if employees == None:
        self.employees = []
       else:
        self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.get_info())   

dev1 = Developer('Komil', 'Komolov', 900000, 'Golang')     
dev2= Developer('Kim', 'Li', 850000, 'Java')   
dev3 = Developer('Bryus', 'Li', 705000, 'C#')   
dev4 = Developer('John', 'Dep', 990000, 'C++')   
dev5 = Developer('Kevin', 'Mackalister', 800000, 'C')   
dev6 = Developer('Eshmat', 'Toshmatov', 250000, 'Ruby')   
dev7 = Developer('Jacky', 'Chan', 90000, 'R')   
dev8 = Developer('Shakhrukh', 'Khan', 700000, 'V')   

man1 = Manager('Yusuf', '.....', 990000)
man1.add_emp(dev1)
man1.add_emp(dev3)
man1.add_emp(dev6)
man1.add_emp(dev8)
man1.print_emps()
man1.del_emp(dev3)
man1.del_emp(dev8)
print()
man1.print_emps()
#print(help(dev1))'''


         ################ 2 - m a s a l a ###################
          ## 1 - u s u l ##

'''class Animal:
    def __init__(self,turi,nomi,voice):
        self.turi = turi
        self.nomi = nomi
        self.voice =  voice
    def full_name(self):
        return f"{self.turi} {self.nomi}"
    def get_info(self):
        return f"{self.full_name()} ning ovozi {self.voice}"

class Wild(Animal):
    def __init__(self,turi, nomi ,voice,qobilyat):
        super().__init__(turi, nomi, voice)
        self.qobilyat = qobilyat
        #print(self.get_info())

    def get_info(self):
        return super().get_info()+f" .{self.full_name()} hayvoni  {self.qobilyat} hususiyati"


class Pet(Animal):
    def __init__(self,turi, nomi ,voice,qobilyat):
        super().__init__(turi, nomi, voice)
        self.qobilyat = qobilyat
        #print(self.get_info())

    def get_info(self):
        return super().get_info()+f" .{self.full_name()} hayvoni  {self.qobilyat} hususiyati"
    def eat(self):
        print("gosht yidi")

wd1 = Wild('sher','yovoyi','arrr','ov qilish')
print(wd1.get_info())
print()
p1 = Pet('Mushuk','uy hayvoni','myaaw myaaw','erkalanish')   
print(p1.get_info())'''


        ## 2 - u s u l ##

'''class Animal:
    def voice(self):
        print("Nimadur")
    def tana(self):
        print("Nimadur")
class dog(Animal):
    def voice(self):
        print("wow wow")
    def tana(self):
        print("Tort oyoq , Uzun va egiluvchan umurtqa")
class ot(Animal):
    def voice(self):
        print("Phffff phffff")
    def tana(self):
        print("Katta va yog'on suyaklar og'ir vazifa uchun")

nima = dog()
nima.voice()
nima.tana()
ot1 = ot()
ot1.voice()
ot1.tana()'''




'''class Bosh:
    def __init__(self,name):
        self.name = name

class Line(Bosh):
    def __init__(self,name):
        super().__init__(name)
        for i in range(4):
            print("*" ,end =" ")


class Triangle(Bosh):
     def __init__(self,name):
        super().__init__(name)
        for i in range(6):
            for j in range(i):
                print("* ", end=" ")
            print()

class Rectangle(Bosh):
     def __init__(self,name):
        super().__init__(name)
        for i in range(4):
            for j in range(4):
                print("* ",end=" ")
            print()

print("""
1.Line
2.Triangle
3.Rectangle
""")
n=int(input("son kiriting: "))
if n==1:
    Line(n)
elif n==2:
    Triangle(n)
else:
    Rectangle(n)'''


'''class Kamanda:
    def __init__(self, nomi, azosi,trener, kapitan):
        self.nomi = nomi
        self.azosi = azosi
        self.trener = trener
        self.kapitan = kapitan

    def full_name(self):
        return f"{self.nomi} {self.azosi}"

    def get_info(self):
        return f"{self.full_name()} {self.trener} {self.kabitan} "
k1 = Kamanda('Barsa',22,'Xavi','Pique')
k2 = Kamanda('Real',19,'Zidan','Marcelo')
k3 = Kamanda('Bavariya',25,'kimdr','Lewandovski')
k4 = Kamanda('City',20,'Gvardiola','De Brunye')
k5 = Kamanda('Liverpool',24,'Y.Klopp','Salah')'''

       
       ######## mini proekt #######

import os
os.system("cls")

class Moshina:
    def __init__(self,nomi) -> None:
        self.nomi = nomi
        self.petrol = 100
        self.engine = False
        self.get_info()
    def get_info(self):
        print(f"Nomi: {self.nomi}\nBenzin: {self.petrol}\nEngine: {bool(self.engine)}")
    def switch_on(self):
        if self.engine == True:
            print("Mashina yoqligan")
        else:
            self.engine += 1
    def switch_off(self):
        if self.engine == False:
            print("Mashina ochiq")
        else:
            self.engine -= 1
    def road(self):
        n = int(input("qancha yol yurasiz: "))
        if n > self.petrol:
            print("There won't be enough petrol!!!")
        if self.engine == False:
            print("Turn on the machine")
        elif n <= self.petrol:
            for i in range(n):
                self.petrol -= i
            print("Yuo've errived")
    def refill(self):
        n = int(input("qancha benzin quyasan: "))
        if n > 100:
            print(f"Extra fuel {((self.petrol + n) - 100)}")
        else:
            self.petrol += n
            print("It is full")

nima = Moshina("BMW M5 F90")

while True:
    print("""
1. Swich on 
2. Swich off
3. Road
4. Refill
5. Just drive
6. Break
""")
    number =int(input("Enter a number: "))
    if number == 1:
        nima.switch_on()
        nima.get_info()
    elif number == 2:
        nima.switch_off()
        nima.get_info()
    elif number == 3:
        nima.road()
        nima.get_info()
    elif number == 4:
        nima.refill()
        nima.get_info()
    elif number == 5:
        nima.switch_on()
        nima.road()
        nima.get_info()
    elif number == 6:
        break




    
    


