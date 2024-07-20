"""
    Python
    link: https://www.python.org/
    Programa que:
    imprima por consola todos los números comprendidos entre 10 y 100 (incluidos), pares, y que no son ni el 66 ni múltiplos de 3.
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Algoritmo:
    1.- Crear una lista con los numeros del 10 al 100 pares    
    3.- Eliminar los multiplos de 3, 66 esta incluido
    4.- imprimir en terminal el resultado.
"""

# funcion crea lista con un rango de numeros y que sean pares
def crear_lista_de_numeros():
    lista_pares=[]    
    print("Ingresa el primer numero")
    num1 = int(input()) 
    print("Ingresa el segundo numero")
    num2 = int(input()) + 1
    # llena la lista con numeros pares    
    for i in range(num1,num2):
        if i % 2 == 0:
            lista_pares.append(i)        
    return lista_pares

# Crea una lista con el resultado de la funcion crear_lista_de_numeros()
lista_pares=crear_lista_de_numeros()

# Imprime la lista original
print("Lista original\n",lista_pares)

# Elimina los numeros multiplos de 3 (incluido el 66) usando remove
for i in lista_pares[:]:
        if i % 3 == 0:
            #print(i)
            lista_pares.remove(i)
            #print(lista_pares)

# Imprime la lista solicitada
print("\nLista solicitada: \n",lista_pares)


