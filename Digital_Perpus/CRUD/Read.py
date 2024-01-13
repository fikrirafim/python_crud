from . import Operasi
    
def read_console():

    print("\n")
    print("="*100)
    no = "No."
    penulis = "Penulis"
    judul = "Judul"
    tahun_terbit = "Tahun Terbit"

    print (f"{no:5} | {penulis:40} | {judul:40} | {tahun_terbit:5}")
    print ("="*100)

    read_data = Operasi.read()
    for no,data in enumerate(read_data) :
        data_break = data.split(",")
        if len(data_break) >= 5:
            primary_key = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break [3]
            tahun_terbit = data_break[4]
            print (f"{no + 1 :5} | {penulis:.40} | {judul:.40} | {tahun_terbit:5}")


    print ("-"*100)