"""
Operadores
"""

#operadores arimetricos
print(f"suma 10 + 3 = {10 + 3}")
print(f"resta 10 - 3 = {10 - 3}")
print(f"multiplicacion 10 * 3 = {10 * 3}")
print(f"divicion 10 / 3 = {10 / 3}")
print(f"modulo 10 % 3 = {10 % 3}")

# operadores de comparacion
print(f"Igualdad: 19 == 19 es {19 == 19}")
print(f"desigualdad : 19 != 19 es {19 != 19}")
print(f"Mayor que: 19 > 10  es {19 > 10}")
print(f"Menor que: 19 < 10 es {19 < 10}")
print(f"Mayor o igual que: 19 >= 10 {19 >= 10}")
print(f"Menor o igual que: 19 <= 10 {19 <= 10}")

#operadores  logicas
print(f"And &&: 10 + 12 == 22 and 5 - 2 == 3 es {10 + 12 == 22 and 5 - 2 == 3}")
print(f"Or ||:10 + 12 == 22 and 5 - 2 == 3 es {10 + 12 == 22 or 5 - 2 == 3} ")
print(f"Not !: not 10 + 12  == 23 { not 10 + 12 == 22}")


# operadores con asignacion 
my_number = 8 # asignacion
print(my_number)

my_number += 2 # suma y asignacion
print(my_number)

my_number -= 4 # resta y asignacion
print(my_number)

my_number *= 3 # multiplicacion y asignacion
print(my_number)

my_number /= 2 # divicion y asignacion
print(my_number)


# operadores con identidad
a = 9
b = 10
# asignamos el is, a es igual que b, esto nos deberia de dar true o false
print(a is b)

#podemos usar el id para indentificar su id
print(id(a))#133673780249072
print(id(b))#133673780249104
# si fuesen iguales los dos tendrian el mismo id

# is not
a = 18
b = 10 

print(a is not b)

# operadores de pertenencia 
# operador in
a = {1, 3 , 4 ,5 ,10, 11}
b = {2, 5, 6 , 8 ,12}

print(10 in b) # nos devolveria false porque 10 no pertence en b 

# operador in not
a = {1, 3 , 4 ,5 ,10, 11}
b = {2, 5, 6 , 8 ,12}

print( 10 not in b) # nos devolveria true porque 10 no pertenece en b y es verdadero


# Condicionales
restriccion_de_edad = 19

if restriccion_de_edad >=18:
    print("Puedes pasar")
elif restriccion_de_edad == 18: 
    print("pasas pero estaras en supervicion")
else:
    print("No puedes pasar")
# Interactivas


# manejo de exepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")


# Extra 
for number in range(10, 55):
    if number% 2 == 0 and number !=16 and number% 3 != 0:
        print(number)