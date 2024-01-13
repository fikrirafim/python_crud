# program untuk membuat database baru bila main.py tidak dapat menemukan file untuk di read
# dipanggil pada program database

from . import Database
from .Util import random_string
import time
import os

def first_data():

        penulis = input("Penulis \t: ")
        judul = input("Judul \t\t: ")
        tahun_terbit = input("Tahun Terbit \t: ")

        data = Database.TEMPLATE.copy()

        data ["primary_key"] = random_string(6)
        data ["date_add"] = time.strftime("%Y-%m-%d-%H-%M%z",time.gmtime())
        data ["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data ["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data ["tahunTerbit"] = tahun_terbit
        
        data_str = f'{data["primary_key"]},{data ["date_add"]},{data ["penulis"]},{data ["judul"]},{data ["tahunTerbit"]}\n'
        print (data_str)
        try :
                with open (Database.DB_NAME,"w",encoding="utf-8") as file :
                        file.write(data_str)

        except : 
                print ("data gagal di tambahkan")
                print ("program end")

# buat data
def create(penulis,judul,tahun_terbit) :
        print ("database created")
        data = Database.TEMPLATE.copy()

        data ["primary_key"] = random_string(6)
        data ["date_add"] = time.strftime("%Y-%m-%d-%H-%M%z",time.gmtime())
        data ["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data ["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data ["tahunTerbit"] = tahun_terbit
        
        data_str = f'{data["primary_key"]},{data ["date_add"]},{data ["penulis"]},{data ["judul"]},{data ["tahunTerbit"]}\n'
        
        try :
                with open (Database.DB_NAME,"a",encoding="utf-8") as file :
                        file.write(data_str)

        except : 
                print ("data gagal di tambahkan")
                print ("program end")


# baca data
def read(**kwargs) :
        try :
                with open (Database.DB_NAME,"r") as file :
                        content = file.readlines()
                        jumlah_buku = len(content)
                        print (f"jumlah data : {jumlah_buku}")

                        if "index" in kwargs :
                                index_buku = kwargs["index"]-1
                                if index_buku < 0 or index_buku > jumlah_buku :
                                        return False
                                else :
                                        return content[index_buku]
                        
                        else :
                                return content

        except : 
                print ("Data gagal di buka")
                return False


#update data
def update(no_buku,primary_key,date_add,penulis,judul,tahun_terbit) :
        data = Database.TEMPLATE.copy()

        data ["primary_key"] = primary_key
        data ["date_add"] = time.strftime("%Y-%m-%d-%H-%M%z",time.gmtime())
        data ["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data ["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data ["tahun_terbit"] = str(tahun_terbit)
        
        data_str = f'{data["primary_key"]},{data ["date_add"]},{data ["penulis"]},{data ["judul"]},{data ["tahun_terbit"]}\n'

        panjangData = len(data_str)

        try :
                with open (Database.DB_NAME,"r+",encoding="utf-8") as file :
                        file.seek (panjangData*(no_buku-1))
                        file.write (data_str)

        except :
                print("Update error")

def delete(no_buku) :
        print (no_buku)
        try :
                with open (Database.DB_NAME, 'r') as file :
                        counter = 0
                        while True :
                                content = file.readline()
                                if len(content) == 0 :
                                        break
                                elif counter == no_buku - 1 :
                                        pass
                                else :
                                        with open ("data_temp.txt",'a',encoding="utf-8") as temp_file :
                                                temp_file.write(content)
                                counter += 1

        except :
                print ("error")

        os.replace("data_temp.txt",Database.DB_NAME)


