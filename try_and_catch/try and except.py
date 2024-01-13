"""
 try and exceptoin (catch) digunakan untuk menghandle sebuah error agar program python 
 bisa tetap berjalan namun dengan peringatan yang lebih mudah di mengerti ketika program mengalami error
"""

# documentation

try :
    # try akan menjalankan nilai true
    with open("datatext.txt",'r') as file :
        file.read()
        print(file)

except :
    # except / catch akan menjalankan sebuah kondisi bila program error
    with open("datatext.txt","w", encoding="utf-8") as file :
        content = file.write("Hello world")
        print (content)