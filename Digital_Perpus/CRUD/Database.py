from . import Operasi

DB_NAME = "databuku.txt"
TEMPLATE = {
    "primary_key" : "XXXXXX",
    "date_add" : "YYYY-MM-DD",
    "judul" : 255*" ",
    "penulis" : 255*" ",
    "tahun_terbit" : "YYYY"
}

def init_console() :
    print("Database Checker")
    try :
        with open (DB_NAME,"r") as file :
            print("Database readable : True")

    except :
        print("Database readable : False, buat database baru")
        Operasi.first_data()