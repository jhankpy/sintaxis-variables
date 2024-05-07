#listas
my_list = ["Jhancarlos","jhank1315@gmail.com",19]
my_list.append("Ocaña") #insertar 
my_list.remove("Ocaña") #eliminar
my_list[2] = 29 # actualizar
print (my_list)

#tuplas

my_tuplas = ("Jhancarlos", "reni", 19, "Anuel")
print(my_tuplas)





# print(my_list[0]) # esto es para buscar dentro de la lista recordar que una lista comienza de 0 a 1
"""esto son diccionarios, tienen su key"""
my_diccionarios = {
    "name" : "jhancarlos",
    "email" : "jhank1315@gmail.com",
    "edad" : 19
} 

# sets

my_sets = {"jhancarlos", "Jhank1315@gmail.com", 19}

my_sets.add("Pineda")
# my_sets = set(sorted(my_sets)) # no ordenado

print(my_sets)

"""Extra"""


def my_agenda():

    agenda = {}
    def inserta_contacto():
        Numero = input("Inserta el numero del contacto:")
        if Numero.isdigit() and len(Numero)> 0 and len(Numero) <= 10:
            agenda[Nombre] = Numero

        else:
            print(f"No se a encontrado {Nombre} en sus contactos")
        
    while True:
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecionas una opcion: ")

        match option:
            case "1":
                Nombre = input("Busca el nombre del contacto aqui:")
                if Nombre in agenda:
                    print(f"el numero del contacto {Nombre} es {agenda[Nombre]}")

                else:
                    print(f"No se a encontrado {Nombre} en sus contactos")
                pass
            case "2":
                Nombre = input("Inserta el nombre del contacto:")
                Numero = input("Inserta el numero del contacto:")
                if Numero.isdigit() and len(Numero)> 0 and len(Numero) <= 10:
                    agenda[Nombre] = Numero
                else:
                    print("Debes intruducir un numero con menos de 11 digitos")
                
                pass
            case "3":
                Nombre = input("Intruduce el nombre del contacto que deseas actualizar:")
                if Nombre in agenda:
                    inserta_contacto()
                pass
            case "4":
                Nombre = input("Intruduce el nombre del contacto que deseas eliminar:")
                if Nombre in agenda:
                    del agenda[Nombre]
                else:
                    print(f"No se a encontrado {Nombre} en sus contactos")
                pass
            case "5":
                break
                print("Saliendo...")
            case _:
                print("porfavor seleciona una opcion valida, 1 a 5")    

my_agenda()
