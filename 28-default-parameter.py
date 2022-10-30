# Belajar Defatult Argument Value

def say_hello(name="sanas"):  # (parameter="parameter defatult")
    print(f"Hello {name}")


say_hello("akmal")
say_hello()


# harus punya default valeu atau default value nya di kosongkan
def say_hello(first_name="sanas", last_name=""):
    print(f"Hello {first_name} - {last_name}")


say_hello("akmal")
say_hello(last_name="febriyan")  # masuk langsung sama nama parameter nya
say_hello(first_name="muhammad", last_name="akmal")
