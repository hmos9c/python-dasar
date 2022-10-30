# Membuat Perogram menggunakan For-Loop, List dan Range

# membuat jumlah data yang ingin di inputkan
banyak = int(input("Berapa banyak data? (contoh = 2) "))

# variabel nama dan umur berupa list
nama = []
umur = []

for i in range(0, banyak):  # melakukan perulangan sebanyaknya input
    print(f"Data ke {i}")

    # meminta nama dan umur setiap datanya
    input_nama = input("Nama : ")
    input_umur = int(input("Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):  # perulangan dan menyatukan data dan string
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")
