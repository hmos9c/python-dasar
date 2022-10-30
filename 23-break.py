# Belajar Break

for i in range(1, 100):
    if i % 50 == 0:
        break  # menghentikan perulangan
    print(i)

while True:
    data = input("Data : ")
    if data == "x":
        break  # menghentikan perulangan
    print(data)
