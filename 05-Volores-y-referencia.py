"""
Valores y referencias
"""
# valor
def doblar_valor(numero):
    numero *= 2

n = 11
doblar_valor(n)
print(n)

# referencia

def doblar_referencias(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [50, 100 , 300]
doblar_referencias(ns)
print(ns)


# Para modificar los tipos simples podemos devolverlos modificados y reasignarlos
def doblar_valor(numero):
    return numero * 2

n = 11
n = doblar_valor(n)
print(n)

#Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia

def doblar_referencias(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [50, 100 , 300]
doblar_referencias(ns[:])# Una copia al vuelo de una lista con [:]
print(ns)

"""
EXTRA
"""

def parametros_definidos(numero):
    numero *= 2

float = True 
print(float)