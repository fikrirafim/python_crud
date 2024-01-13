from .import Operasi
from .import Read

def create_console() :
    print ("Silahkan Masukan Data")
    print ("="*30)

    ngulang = True
    while ngulang :
        try :
            penulis = input ("Penulis\t\t : ")
            judul = input ("Judul\t\t : ")
            tahun_terbit = int(input ("Tahun terbit\t : "))

            if len(str(tahun_terbit)) <= 4 :
                ngulang = False
            
            else :
                print ("Tahun harus terdiir 4 digit atau kurang")

                massage = input("ulangi aksi? (y/n)") 

                if massage == "y" :
                    ngulang = True

                elif massage == "n" :
                    ngulang = False

                else :
                    print ("Perintah tidak dikenal")
                    print ("Program closed")
                    break

        except : 
            print ("Tahun wajib berupa angka!")
            print ("Data restart")
    
    Operasi.create(penulis,judul,tahun_terbit)
    print ("="*30,"\n")
    print ("data berhasil ditambahkan\n")
    Operasi.read()
