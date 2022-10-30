# Belajar Membuat Method / Function

nama = []


def print_nama():  # method/function
    print("===================")
    for data in nama:
        print(data)


nama.append("sanas")
print_nama()  # memanggil method

nama.append("feb")
print_nama()

nama.append("riyan")
print_nama()
