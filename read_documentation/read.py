# open / read file
print("baca file")

file = open("data.txt",mode="r")
print (f"read status    : {file.readable()}")
print (f"read status    : {file.writable()}")

# baca semua line
# print (file.read())

# hanya membaca per 1 line saja
#print (file.readline(),end="") 
#print (file.readline(),end="")
#print (file.readline(),end="")
#print (file.readline(),end="") # method end = "" di buat untuk menghapus endline ketika memanggil data yang ada di file

# membuat isi dari file menjadi sebuah data list
print (file.readlines(),)
file.close
if file.close == False :
    print (f"file closed = {file.closed}")

# open file dengan menggunakan with
print ("\nopen file dengan with")
# fungsi dari operator with tidak perlu mendeklarasikan file.close untuk menutup file
with open ("data.txt",mode = "r") as file : 
    content = file.readlines()
    print (content, end="")
