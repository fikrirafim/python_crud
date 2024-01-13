from .import Operasi
from .import Read

def update_console() :
    Read.read_console()

    while True :
        print (" ")
        no_buku = int(input("Pilih data yang ingin di update/dirubah : "))
        data_buku = Operasi.read(index = no_buku)
        
        if data_buku :
            break
        else :
            print ("data tidak ada dalam jangkauan")

    data_break = data_buku.split(",")

    primary_key = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun_terbit = data_break[4] [:-1]

    ngulang = True
    while True :
        print ("\npilih data yang akan di rubah")

        print (f"1. Judul\t: {judul:.40}")
        print (f"2. Penulis\t: {penulis:.40}")
        print (f"3. Tahun_Terbit\t: {tahun_terbit:.4}")

        pilih = input("Pilih (1,2,3) : ")

        match pilih :
            case "1" : judul = input ("Judul\t\t: ")
            case "2" : penulis = input ("Penulis\t\t: ")
            case "3" : tahun_terbit = input ("Tahun terbit\t:")
            case _ : 
                print ("pilihan tidak tersedia")

        massage = input("\nRubah lagi ? [yes/no] : ")

        if massage == 'y' or massage == 'Y' or massage == 'yes' or massage == 'Yes'or massage == ' YES' : 
            ngulang

        elif massage == 'n' or massage == 'N' or massage == 'no' or massage == 'No' or massage == 'NO' :
            print ("\nUpdate berhasil")
            break
        
        else :
            print("not identify")
            break

        
        print ("\nData telah di rubah")
    Operasi.update(no_buku,primary_key,date_add,penulis,judul,tahun_terbit)
    

