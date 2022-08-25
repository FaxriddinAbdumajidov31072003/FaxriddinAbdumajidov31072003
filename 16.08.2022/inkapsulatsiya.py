import os
os.system('cls')

'''class Card:
    def __init__(self,nomi,k_nomer,mudati,):       
        self.nomi = nomi
        self.nomer = k_nomer
        self.mudati = mudati
        self.__code = 1111
        self.__balans = 0
    def get_info(self):
        print(f"nomi: {self.nomi} nomeri{self.nomeri} mudati{self.mudati}")
    
    def kod(self,new):
       self.__code = new
       return self.__code
        
    def get_pass(self):
        return self.__code
    
    def set_plus(self,qancha):
        self.__balans+=qancha
        return self.__balans

    def set_minus(self,qancha):
        self.__balans-=qancha
        return self.__balans

card = Card('uzcard',8600,'1 yil')
card.kod(1234)
print(card.get_pass())
print(card.set_plus(12000))'''


'''class Card:
    def __init__(self,nomi):
       self.nomi = nomi
       self.__code = 1111
       self.__balans = 500000

    def get_info(self):
        return f"nomi: {self.nomi} "

    def kod(self,new):
       self.__code = new
       return self.__code

    def get_sum(self):
        return self.__balans
        
    def get_pass(self):
        return self.__code
    
    def set_plus(self,qancha):
        self.__balans+=qancha
        return self.__balans

    def set_minus(self,qancha):
        self.__balans-=qancha
        return self.__balans


class Odam:
    def __init__(self,ismi):
        self.ism = ismi
        
        self.__sum = 50000

    def get_sum(self,sum):
        self.__sum+=sum
        return self.__sum

    def set_sum(self):
        return self.__sum

class Bankomat:
    def __init__(self):
        self.__zahira = 1_000_000_000

    def change(self,karta):
        n = int(input("yangi kodni kiriting: "))
        card.kod(n)

    def get_zahira(self):
        return self.__zahira

    def set_zahira(self,sum):
        self.__zahira -= sum
        return self.__zahira

    def vazifa(self):
        
        n = int(input("parolni kiriting: "))
        if n==card.kod():
            if sum == card.get_sum() and sum<=self.get_zahira():
                self.set_zahira(sum)
                card.set_plus(sum) 
                odam.get_sum(sum)
            
card = Card('uzcard')
odam = Odam('Komil')  
qaysi = Bankomat()
print(card.get_pass())
qaysi.vazifa()
print(qaysi.get.zahira())
print(odam.get_sum())'''



          ######### 2 - variant  ###############3


'''class Karta:
    def __init__(self,nomi) -> None:
        self.nomi = nomi
        self.code = 1111
        self.__balans = float(500_000)
    def get_parol(self):
        return self.__code
    def get_sum(self):
        return self.__balans
    def set_parol(self,parol):
        self.__code = parol
        return self.__code
    def set_sum_plus(self,sum):
        self.__balans += sum
        return self.__balans
    def set_sum_minus(self,sum):
        self.__balans -= sum
        return self.__balans

class Odam:
    def __init__(self,ismi) -> None:
        self.ismi = ismi
        self.naxt_pul = 50_000
    def get_naxt_pul(self):
        return self.__naxt_pul
    def set_naxt_pul_plus(self,sum):
        self.__naxt_pul += sum
        return self.__naxt_pul

class Bankomat:
    def __init__(self) -> None:
        self.__zaxira = 100_000_000_000_000
    def change(self):
        n = int(input("Yangi parol kiriting: "))
        nima.set_parol(n)
    def get_zaxira(self):
        return self.__zaxira
    def set_zaxira(self,sum):
        self.__zaxira -= sum
        return self.__zaxira
    def vazifa(self):
        sum = int(input("Nechi pul olasan: "))
        n = int(input("Parolni kiritin: "))
        if n == nima.get_parol():
            if sum <= nima.get_sum() and sum <= self.get_zaxira():
                self.set_zaxira(sum)
                nima.set_sum_plus(sum)
                kim.set_naxt_pul_plus(sum)
        
nima = Karta("HUMO")
kim = Odam("Komil")
qaysi = Bankomat()
print(nima.get_parol())
qaysi.change()
qaysi.vazifa()
print(qaysi.get_zaxira())
print(kim.get_naxt_pul())
print(nima.get_sum())'''
    

  #################### APTEKA ####################



        

'''class Apteka:
    def __init__(self, nomi,kassasi):
        self.nomi = nomi
        self.__kassa = kassasi
        self.dorilar_soni = 0
        self.dorilar = []
    
    def set_kassa_plus(self,sum):
        self.__kassa += sum
        return self.__kassa
    def set_kassa_minus(self,sum):
        self.__kassa -= sum
        return self.__kassa


    def add_dori(self,dori):
        self.dorilar.append(dori.info())
        print(dori.ismni_qaytar(), self.nomi, "sotildi")
        self.t_soni+=1

    def delete_dori(self,dori):
        self.dorilar_soni-=1
        self.dorilar.remove(dori.info())

    
def info(self):
        print(f"""
        dori nomi -> {self.nomi}
        Kurs narxi -> {self.narxi}
        Dorilar soni -> {self.dorilar_soni}
        Dorilari -> {self.dorilar}
        """)


class Dori:
    def __init__(self, ism, narxi):
        self.ism = ism
        self.narx = narxi
    
    def ismni_qaytar(self):
        return self.ism

    def narxni_qaytar(self):
        return self.narx

    def info(self):
        return f"{self.ismni_qaytar()} {self.narxni_qaytar()}"


class Odam:
    def __init__(self,nomi ,puli):
        self.nomi = nomi 
        self.__pul = 100000

    def naqt_puli_minus(self,sum):
        self.__pul-=sum
        return  self.__pul

    def sotib_olish(self,dori,apteka):
        apteka.delete_dori(dori.info())
        apteka.set_kassa_plus(dori.narxni_qaytar())
        self.naqt_puli_minus(dori.narxni_qaytar())

d1 = Dori('trimol',5000)
d2 = Dori('fanigan',10000)
d3 = Dori('mezim',15000)
d4 = Dori('sitromon',4000)
d5 = Dori('rinoksil',30000)

a1 =Apteka
a1.add_dori(d1)
a1.add_dori(d3)
a1.add_dori(d5)'''



     

'''class Dori:
  def __init__(self,nomi,narxi,miqdori) -> None:
    self.nomi = nomi
    self.narxi = narxi
    self.miqdori = miqdori

class Odam:
  def __init__(self,puli) -> None:
    self.__puli = puli
  def get_pul(self):
    return self.__puli
  def set_pul(self,pul):
    self.__puli = pul
  def sotib_olish(self,dorixona,dori,soni):
    dorixona.sotish(self,dori,soni)
    

class Apteka:
  def __init__(self,nomi,kassa) -> None:
    self.nomi = nomi
    self.__kassa = kassa
    self.royhat = {}
  
  def get_kassa(self):
    return self.__kassa
  def set_kassa(self,kassa):
    self.__kassa = kassa
  def qoshish(self,dori):
    self.royhat[dori.nomi] = {}
    self.royhat[dori.nomi]['narxi'] = dori.narxi
    self.royhat[dori.nomi]['miqdori'] = dori.miqdori
  def sotish(self,odam,dori,soni):
    if(self.royhat[dori.nomi]['miqdori']<soni):
      print("Bizda buncha dori yo'q")
      return
    if(self.royhat[dori.nomi]['narxi']*soni>odam.get_pul()):
      print("Pulingiz yetarli emas")
      return
    pul = odam.get_pul() - self.royhat[dori.nomi]['narxi']*soni
    odam.set_pul(pul)
    kassa = self.get_kassa() + self.royhat[dori.nomi]['narxi']*soni
    self.set_kassa(kassa)
    self.royhat[dori.nomi]['miqdori']-=soni



fanigan = Dori("fanigan",10000,10)
trimol = Dori("trimol",1000,50)
kyupen = Dori("kyupen",5000,8)
nimisil = Dori("nimisil",5000,60)

Dorixona = Apteka("Dorixona",200000)

Faxriddin = Odam(100000)


Dorixona.qoshish(fanigan)
Dorixona.qoshish(trimol)
Dorixona.qoshish(kyupen)
Dorixona.qoshish(nimisil)

Faxriddin.sotib_olish(Dorixona,fanigan,3)
print(f"kassa {Dorixona.get_kassa()}")
print(f"puli {Faxriddin.get_pul()}")
print(Dorixona.royhat)'''



























