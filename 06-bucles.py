animales = ["zorro", "perro", "gato", "leon"]
numeros = [2,3,5,6]

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a : {animal}")

#recorriendo la lista numeros y multiplando cada valor x10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo la listas numeros y animales al mismo tiempo 
for numero, animal in zip(numeros, animales):
    print(f"recorriendo lista 1 : {numero}")
    print(f"recorriendo lista 2 : {animal}")

# forma correcta de recorrer un indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice del numero es : {indice} y el valor es: {valor}")