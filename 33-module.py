# Belajar Module

# import satu-satu modul
from function_33 import total
from function_33 import say_hello

# import semua modul
import function_33

hello = function_33.say_hello("sanas")
print(hello)

hasil = function_33.total(1, 2, 3, 4, 5)
print(hasil)

# import satu2
hello = say_hello("sanas")
print(hello)

hasil = total(1, 2, 3, 4, 5)
print(hasil)
