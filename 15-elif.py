# Belajar Elif == else if

menu_pilihan = input("silakan pilih menu (1-3) : ")

if menu_pilihan == "1":
    print("anda memilih menu 1")

# elif, agar program ke bawah tidak di eksekusi
elif menu_pilihan == "2":
    print("anda memilih menu 2")

elif menu_pilihan == "3":
    print("anda memilih menu 3")

else:
    print("menu tidak tersedia")

if menu_pilihan == "x": # di anggap blok baru
    print("program keluar")
