# Belajar Tipe Data Dictionary

from email.headerregistry import Address
from multiprocessing.sharedctypes import Value


costumer = {"name": "sanas", "age": 22, "address": "jakarta"}  # dictionary

name = costumer["name"]
age = costumer["age"]
address = costumer["address"]

costumer["company"] = "x"  # tambah data
costumer["name"] = "sanas febriyan"  # ubah data

for key in costumer:
    value = costumer[key]
    print(f"{key}:{value}")

# atau

for key in costumer.items():
    print(f"{key[0]}:{key[1]}")

del costumer["address"]  # hapus data

# atau

for key, value in costumer.items():
    print(f"{key}:{value}")
