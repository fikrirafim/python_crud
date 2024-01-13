from .import Operasi
from .import Read

def delete_console() : 
    Read.read_console()

    ngulang = True
    while ngulang :
        print (" ")
        no_buku = int(input("Pilih data yang ingin di dihapus : "))
        data_buku = Operasi.read(index = no_buku)
        
        if data_buku :
            data_break = data_buku.split(",")

            primary_key = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun_terbit = data_break[4] [:-1]


            print ("\nKamu memilih data berikut")

            print (f"1. Judul\t: {judul:.40}")
            print (f"2. Penulis\t: {penulis:.40}")
            print (f"3. Tahun_Terbit\t: {tahun_terbit:.4}")

            massage = input("Hapus Data ? [yes/no] : ")

            if massage == 'y' or massage == 'Y' or massage == 'yes' or massage == 'Yes'or massage == ' YES' : 
                print ("\nHapus berhasil")
                Operasi.delete(no_buku)
                
                ngulang = False

            elif massage == 'n' or massage == 'N' or massage == 'no' or massage == 'No' or massage == 'NO' :
                ngulang
                
            else :
                print("not identify")
                break
        else :
            print ("data tidak ada dalam jangkauan")