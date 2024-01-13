# Program Database CRUD  PERPUSTAKAAN

import os
import CRUD as CRUD
from CRUD import Read 

if __name__ == "__main__" :

    CRUD.init_console()

    ngulang = True
    os.system("cls")

    while ngulang :

        print("MENU\n")
        print("(1) Buat Data")
        print("(2) Lihat Data")
        print("(3) Rubah Data")
        print("(4) Hapus Data\n")

        print ("WELLCOME TO DIGITAL PERPUS")
        print ("SELECT ACTION\n\n")
        user_input = int(input(f"Action : "))
        print("="*30)

        match user_input :
            case 1 : print(f"\n{CRUD.create_console()}\n")
            case 2 : print(f"\n{CRUD.read_console()}\n")
            case 3 : print(f"\n{CRUD.update_console()}\n")
            case 4 : print(f"\n{CRUD.delete_console()}\n")

        print("\n")

        massage = input("Choose Action ? [yes/no] : ")

        if massage == 'y' or massage == 'Y' or massage == 'yes' or massage == 'Yes'or massage == ' YES' : 
            ngulang

        elif massage == 'n' or massage == 'N' or massage == 'no' or massage == 'No' or massage == 'NO' :
            print ("program selesai")
            ngulang = False
        
        else :
            print("not identify")
            break
