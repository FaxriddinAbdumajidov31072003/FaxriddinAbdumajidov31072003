# import sqlite3

# connection = sqlite3.connect("nimadur.db")
# print(connection)

# import sqlite3

# class DBConnection:
#     def __init__(self):
#         self.__connect()
#     def __connect(self):
#         self.__connection = sqlite3.connect("nimadur.db")

#     def get_connection(self):
#         return self.__connection

# db1 = DBConnection()
# print(db1.get_connection())

#commit - tasdiqlash


import os
os.system ('cls')


import sqlite3

# class DBConnection:
#     def __init__(self):
#         self.__connect()
#     def __connect(self):
#         self.__connection = sqlite3.connect("nimadur.db")
#         self.cursor = self.__connection.cursor()
#     def get_connection(self):
#         return self.__connection

#     #def close(self):
#      #   self.__connection.close()

#     def create_table(self):
#         query = """
#         CREATE TABLE IF NOT EXISTS students(
#             id integer PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             phone_num TEXT
#         );
#         """
#         self.cursor.execute(query)
#         self.__connection.commit()

#     def insert_data(self,name,phone):
#         self.cursor.execute(f"""
#         INSERT INTO students(name,phone_num)
#         VALUES("{name}", '{phone_num}');
#         """)
        
#         self.__connection.commit()

# if __name__ == "__main__":
#     db1 = DBConnection()
#     print(db1.get_connection())
#     db1.create_table()
#     name = input("ismingizni kiriting: ")
#     phone_num = input("raqamingizni kiriting: ")
#     db1.insert_data(name, phone_num)



'''class DBConnection:
    def __init__(self):
        self.__connect()
    def __connect(self):
        self.__connection = sqlite3.connect("nimadur.db")
        self.cursor = self.__connection.cursor()
    def get_connection(self):
        return self.__connection

    #def close(self):
     #   self.__connection.close()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students(
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_num TEXT
        );
        """
        self.cursor.execute(query)
        self.__connection.commit()

    def insert_data(self,name,phone):
        self.cursor.execute(f"""
        INSERT INTO students(name,phone_num)
        VALUES("{name}", '{phone}');
        """)      
        self.__connection.commit()

    def select_all(self):
        self.cursor.execute("SELECT * FROM students;")
        natija = self.cursor.fetchall()
        print(natija)

    def select_one(self):
        self.cursor.execute("SELECT * FROM students;")
        natija = self.cursor.fetchone()
        print(natija)
        print(self.cursor.fetchone())


    def select_many(self,nechta):
        self.cursor.execute('SELECT * FROM students;')
        natija = self.cursor.fetchmany(nechta)
        print(natija)

    def select_teskari(self):
        self.cursor.execute('SELECT * FROM students order by id desc')
        a = self.cursor.fetchmany(50)
        print(a)

    def colect_delete(self):
        self.cursor.execute('SELECT * FROM students;')
        a = self.cursor.fetchall()
        # for i in a:
        #     print(i[-1])
        # n = input("qaysi raqamni ochirsiz:  ")
        self.cursor.execute(f"delete from students where {n} = phone_num")
        self.__connection.commit()

    def update(self):
        n = input("ismini yozing: ")
        n2 = input("yangi nomer kirit: ")
        self.cursor.execute(f"update students set phone_num = '{n2}' where name = '{n}';")


if __name__ == "__main__":
    db1 = DBConnection()
    #print(db1.get_connection())
    #db1.create_table()
    db1.select_all()
    db1.update()
    db1.select_all()
    #db1.colect_delete()
    #db1.select_teskari()  
    for i in range(4):
        name = input("ismingizni kiriting: ")
        phone_num = input("raqamingizni kiriting: ")
        db1.insert_data(name, phone_num)'''

 
 #import mysql.connector


# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="yusuf6451895"
# )

# print(connection)

####################################################################################################

# import sqlite3

# connection = sqlite3.connect("nimadur.db")
# print(connection)


# import mysql.connector

# class DBConnection:
#     __DB_NAME = "found57"
    
#     def __init__(self):
#         self.__connect()
#         self.__create_DB_use()

#     def __connect(self):
#         self.__connection = mysql.connector.connect(
#            host="localhost",
#            user="root",
#            password="yusuf6451895" 
#         )
#         self.cursor = self.__connection.cursor()
    
#     def __create_DB_use(self):
#         self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__DB_NAME};")
#         self.cursor.execute(f"USE {self.__DB_NAME};")

#     def create_table(self):
#         query = """
#         CREATE TABLE IF NOT EXISTS students(
#             id int PRIMARY KEY AUTO_INCREMENT,
#             name TEXT,
#             phone_num TEXT
#         );
#         """
#         self.cursor.execute(query)
#         self.__connection.commit()

#     def insert_data(self, name, phone):
#         self.cursor.execute(f"""
#         INSERT INTO students(name, phone_num) 
#         VALUES("{name}", '{phone}');
#         """)
#         self.__connection.commit()
    

#     def select_all(self):
#         self.cursor.execute("SELECT * FROM students;")
#         natija = self.cursor.fetchall()
#         print(natija)
#         # for i in natija:
#         #     print(i[-1])

#     def select_one(self):
#         self.cursor.execute("SELECT * FROM students;")
#         natija = self.cursor.fetchone()
#         print(natija)
#         print(self.cursor.fetchone())
#         print(self.cursor.fetchone())

#     def select_many(self, nechta):
#         self.cursor.execute('SELECT * FROM students;')
#         natija = self.cursor.fetchmany(nechta)
#         print(natija)
    
#     def oxir_nechta(self, nechta):
#         self.cursor.execute(f"Select * from students order by id desc limit {nechta}")
#         natija = self.cursor.fetchall()
#         print(natija)

#     def delete_by_phone(self, nomer):
#         self.cursor.execute(f"DELETE FROM students WHERE phone_num={nomer};")
#         self.__connection.commit()

#     def get_connection(self):
#         return self.__connection
    
# if __name__ == "__main__":    
#     db1 = DBConnection()
#     db1.create_table()
#     # for i in range(5):
#     #     name = input("Ismingizni kiriting: ")
#     #     phone = input("Raqamingizni kiriting: ")
#     #     db1. insert_data(name, phone)
#     # db1.select_all()
#     # db1.select_one()
#     # db1.select_many(3)
#     # db1.oxir_nechta(4)
#     db1.delete_by_phone('+998933655652')
#     db1.select_all()


# Algorithms

# -Searching algorithms
#     Linear
#     Binary


# -Sorting algorithms
#     Bubble sort
#     Selection sort
#     Isertion sort
#     Quick sort



# def LinearSearch(lst, element):
#     for i in range(lst):
#         if lst[i] == element:
#             return i
#     return -1




# def BinarySearch(lst, val):
#     first = 0
#     last = len(lst)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         print(mid)

#         if lst[mid] == val:
#             index = mid
#         else:
#             if val<lst[mid]:
#                 last = mid-1
#             else:
#                 first = mid+1
    
#     return index



# lst = [10,20,33,41,57,60,71,89,90,100]
# natija = BinarySearch(lst, 33)
# if natija == -1:
#     print('Siz qidirgan son mavjud emas')
# else:
#     print(f"Siz qidirgan son [{natija}] - indexda joylashgan")









