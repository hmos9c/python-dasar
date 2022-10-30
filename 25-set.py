# Belajar Set

# list => []
# tuple => ()
# set => {}

# set tidak bisa memasukan data yang sama, tidak akan menerima data duplikat

nama = {"sanas", "akmal", "sanas", "akmal", "ardi"}

print(nama)
# data set tidak bisa menjamin ordernya, index berubah-rubah

# print(nama[0])
# set tidak mendukung pengambilan data menggunakan index

# menambah data menggunakan add
nama.add("balqis")
for data in nama:
    print(data)

# menghapus data menggunakan remove
nama.remove("sanas")

print(nama)
