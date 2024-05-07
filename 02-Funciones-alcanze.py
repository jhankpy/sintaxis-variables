#simple
def prm_greet():
    print("Hola mundo")

prm_greet()

#con retorno
def return_greet():
    return "Hola, mundo"



# con argumento
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Jhan")
#con argumentos
def args_greet(greet, name):
    print({greet}, {name})

args_greet("Hola","Noah")

#Local y gloval

my_global = "Jhancarlos"

def my_glb():
    local= "Hola"
    print(f"{local}, {my_global}")# el global y el local sirve dentro de una funcion
print(my_global)# y si lo hacemos afuera no sirva solo el global mas no el local
my_glb()

#Extre 
def ext_greet(texto1, texto2) -> int:
    count = 0
    for number in range(1, 101):
        if number% 3 == 0 and number% 5 == 0:
            print(texto1,texto2)
        elif number% 3 == 0:
            print(texto1)
        elif number% 5 == 0:
            print(texto2)
        else:
            print(number)
            count += 1
    return count 

print(ext_greet("texto 1", "texto 2"))