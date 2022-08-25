'''class Avto:
   model = 'Mers'
   speed = 340
   color = 'black'
   cost = 20000
Audi = Avto
Audi.model = 'Audi'
Audi.speed =320
Audi.color = 'silver'
Audi.cost = 25000
print(f"model:",Audi.model)
print(f"max speed:",Audi.speed)
print(f"color:",Audi.color)
print(f"cost $",Audi.cost)'''


'''class Animal:
    nomi = 'tiger'
    turi = 'wild'
    weight = 150 
Lion = Animal
Lion.nomi = 'lion'
Lion.turi = 'wild'
Lion.weight = 180

cat = Animal
cat.nomi= 'qoplon'
cat.turi = 'Uy hayvoni'
cat.weight = 3

print(Lion.weight)''' #ohirgisini ozlashtirib qoyadi 

         ################ 1 - m a s a l a ###########################

'''class Avto:
    def __init__(self, name  , color):
        self.ism = name
        self.rang = color
    def clear(self):
        print(f"{self.ism} cleared")
    def colour(self):
        print(f"{self.ism} color is {self.rang}")      
BMW = Avto('BMW', 'black')
lexus = Avto('lexus', 'white')
lexus.clear()
lexus.colour()
BMW.colour()'''

               ############### 2 - m a s a l a ##################

'''class student:
    def __init__(self, name,surname , age, kurs,ball):
        self.ism = name
        self.surname = surname
        self.age = age 
        self.kurs = kurs
        self.ball = ball
    def full_name(self):
        return (f"{self.ism} {self.surname}")
    def kurs_update(self):
        if self.balni_et()>56:
            self.kurs+=1
        else:
            print("fault in exam")
    def yosh(self):
        return self.age
    def balni_et(self):
        return self.ball
    def info(self):
        print(f"{self.full_name()} {self.age} {self.kurs} {self.ball}")

komil=student('komil','komilov',18,1,54)
komil.kurs_update()
komil.info()'''


         ##################### 3 - m a s a l a ####################

'''class Kurs:
    def __init__(self, nomi, ustozi):
        self.nomi = nomi
        self.ustoz = ustozi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self, talaba):
        self.talabalar.append(talaba.full_name())
        print(talaba.ismni_qaytar(), self.nomi, "KURSIGA QABUL QILINDI")
        self.talabalar_soni+=1

    def delete_student(self, talaba):
        self.talabalar_soni-=1
        self.talabalar.remove(talaba.full_name())

    

    def info(self):
        print(f"""
        Kurs nomi -> {self.nomi}
        Kurs ustozi -> {self.ustoz}
        O'quvchilar soni -> {self.talabalar_soni}
        O'quvchilari -> {self.talabalar}
        """)


class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
    
    def ismni_qaytar(self):
        return self.ism

    def familiyani_qaytar(self):
        return self.familiya

    def full_name(self):
        return f"{self.ismni_qaytar()} {self.familiyani_qaytar()}"


class Hayvon:
    def __init__(self, nomi, rangi):
        self.nomi = nomi
        self.rangi = rangi

    def full_name(self):
        pass
    

GO = Kurs("GO-5", "Nurali")
JAVA = Kurs("Java-4", "Abdulvahid")
FLUTTER = Kurs("Flutter-7", "Kimdur")
QA = Kurs("QA-1", "Kimdur2")

Muslima = Talaba("Muslima", "Abdurahimova")
Bahodir = Talaba("Bahodir", "Amirov")
Faxriddin = Talaba("Faxriddin", "Abdumajidov")
Muhammadrizo = Talaba("Muhammadrizo", "Abdurazzoqov")
Shaxboz = Talaba("Shaxboz", "Mamatkarimov")
Sherzod = Talaba("Sherzod", "Rahmonov")
Madina = Talaba("Madina", "Abduqahhorova")
Iroda = Talaba("Iroda", "Fatxullayeva")
Saidali = Talaba("Saidali", "Abdullayev")
Rahimjon = Talaba("Rahimjon","Xolmatjonov")
Javohir = Talaba("Javohir", "Mengliboyev")
Saidamirxon = Talaba("Saidamirxon", "Ne'matullayev")

# MUSHU = Hayvon("Mosh", "QORA")

JAVA.add_student(Saidamirxon)
JAVA.add_student(Javohir)
GO.add_student(Rahimjon)
FLUTTER.add_student(Saidali)
JAVA.add_student(Iroda)
FLUTTER.add_student(Madina)
JAVA.add_student(Sherzod)
GO.add_student(Shaxboz)
QA.add_student(Muhammadrizo)
QA.add_student(Faxriddin)
QA.add_student(Bahodir)
FLUTTER.add_student(Muslima)


QA.delete_student(Bahodir)

QA.info()
FLUTTER.info()
JAVA.info()
GO.info()'''

            ################# 4 - m a s a l a  ###################      

'''class Kurs:
    def __init__(self, nomi, ustozi):
        self.nomi = nomi
        self.ustoz = ustozi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self, talaba):
        if talaba.ball>56:
            self.talabalar.append(talaba.full_name())
            self.talabalar_soni+=1
            print(talaba.ismni_qaytar(), self.nomi, "KURSIGA QABUL QILINDI")
            self.talabalar_soni+=1
        

    def delete_student(self, talaba):
        pass
        
    def info(self):
        print(f"""
        Kurs nomi -> {self.nomi}
        Kurs ustozi -> {self.ustoz}
        O'quvchilar soni -> {self.talabalar_soni}
        O'quvchilari -> {self.talabalar}
        """)


class Talaba:
    def __init__(self, ism, familiya,ball):
        self.ism = ism
        self.familiya = familiya
        self.ball = ball

    def ball(self):
        return self.ball


    def ismni_qaytar(self):
        return self.ism

    def familiyani_qaytar(self):
        return self.familiya

    def full_name(self):
        return f"{self.ismni_qaytar()} {self.familiyani_qaytar()}"


class Hayvon:
    def __init__(self, nomi, rangi):
        self.nomi = nomi
        self.rangi = rangi

    def full_name(self):
        pass
    

GO = Kurs("GO-5", "Nurali")
JAVA = Kurs("Java-4", "Abdulvahid")
FLUTTER = Kurs("Flutter-7", "Kimdur")
QA = Kurs("QA-1", "Kimdur2")

Muslima = Talaba("Muslima", "Abdurahimova",34)
Bahodir = Talaba("Bahodir", "Amirov",58)
Faxriddin = Talaba("Faxriddin", "Abdumajidov",90)
Muhammadrizo = Talaba("Muhammadrizo", "Abdurazzoqov",70)
Shaxboz = Talaba("Shaxboz", "Mamatkarimov",78)
Sherzod = Talaba("Sherzod", "Rahmonov",34)
Madina = Talaba("Madina", "Abduqahhorova",21)
Iroda = Talaba("Iroda", "Fatxullayeva",59)
Saidali = Talaba("Saidali", "Abdullayev",34)
Rahimjon = Talaba("Rahimjon","Xolmatjonov",23)
Javohir = Talaba("Javohir", "Mengliboyev",11)
Saidamirxon = Talaba("Saidamirxon", "Ne'matullayev",57)

# MUSHU = Hayvon("Mosh", "QORA")

JAVA.add_student(Saidamirxon)
JAVA.add_student(Javohir)
GO.add_student(Rahimjon)
FLUTTER.add_student(Saidali)
JAVA.add_student(Iroda)
FLUTTER.add_student(Madina)
JAVA.add_student(Sherzod)
GO.add_student(Shaxboz)
QA.add_student(Muhammadrizo)
QA.add_student(Faxriddin)
QA.add_student(Bahodir)
FLUTTER.add_student(Muslima)




QA.info()
FLUTTER.info()
JAVA.info()
GO.info()'''



