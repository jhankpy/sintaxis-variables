"""
Operaciones
"""
# primera cadena con ""
my_cadena = "Hola mundo"
print(my_cadena)
print(type(my_cadena))

#segunda cade con '' tambien es valida
my_cadena2 = 'Hola munda 2'
print(my_cadena2)
print(type(my_cadena2))

# primera y segunda linea
my_linea = "Hola mundo \n Como estan"
print(my_linea)

#formateo de cadenas 
x= 4
y = "El numero es: " + str(x)
print(y)

# Métodos

my_metodos = "hola mundo"

print(my_metodos.title())# nos entrega los primeros caracter en mayuscula

print(my_metodos.capitalize())# nos entrega el primer caracter en mayuscula

print(my_metodos.lower()) # convierte los carecteres alfabeticos en minisculas

print(my_metodos.upper()) # nos entrega todo los carateres en mayusculas



#cocantedacion
s1 = "Hola"
s2 = "Python"

print(s1 + "", s2 + "!")
# repiticion 

print(s1 * 3)

# Indexacion
print(s1[0] + s1[2]+ s1[1])

# Longitud

print(len(s1))

# slicing 

print(s2[1:4])

# busqueda
print("h" in s2)
print("i" in s1)

# remplazo 
print(s1.replace("o", "a"))

# divicion
print(s2.split("h"))

# Eliminacion de espacios al principio y al final
print("   Hola Mundo    ".strip())

# busqueda de posicion 
print("Hola mundo como estan".find("como"))
print("Hola mundo como estan".find("n"))


s3 = "Hola mundo como estan"
# busqueda de ocurrencias

print(s3.count("H"))
print(s3.count("a"))

#interpolacion
print(f"Saludo: {s1}, Lenguaje: {s2}")
s4 = "Jhancarlos","Jose", "Maria"

#transformacion en lista de caracteres
print(list(s3))

# transformacion en lista en cadena 
print("".join(s4))


# transformacion numerica 
n1= "12345678910"
n1 = int(n1)
print(n1)

#comparacion varias
print(s1.isalnum())
print(s1.isalpha())


"""
Extra
"""

def palch(work1: str , work2: str ):

    #Palíndromos
    print(f"¿{work1} es un palindromo : {work1 == work1[: : -1]}")
    print(f"¿{work2} es un palindromo : {work2 == work2[: : -1]}")

    #Anagrama
    print(f"¿{work1} es un anagrama de {work2}: {sorted(work1) ==  sorted(work2)}")

    #Isograma
    print(f"¿{work1} es un isograma : {len(work1) ==  len(set(work1))}")
    print(f"¿{work2} es un isograma : {len(work2) ==  len(set(work2))}")
    
palch("radar", "darar")
#palch("azucar", "caruza")


def saludo():
    Nombre = input ("\nHola inserta tu nombre:")
    print(f"\n hola como estas {Nombre}")

saludo()