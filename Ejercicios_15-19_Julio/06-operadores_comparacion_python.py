"""
    Ejemplos de uso de operadores en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Operadores de Comparacion en Python
    > Mayor que
    >= Mayor o igual que
    < Menor que
    <= Menor o igual que
    == Igual
    != Distinto
"""
# Comparación

numero_01 = 14
numero_02 = 5

mayor_que = numero_01 > numero_02 
mayor_igual_que = 14 >= 5
menor_que = 14 < 5
menor_igual_que = 14 <= 5
igual = 14 == 5
distinto = 14 != 5

print("Operadores de Comparación")

"""
    Se crean dos listas, la primera contiene el titulo de la operacion de comparación y la segunda el resultado
"""

# Lista de operandos de Comparación
nombre_comparacion = [f"Mayor que: {numero_01}>{numero_02} = ", f">= Mayor o igual que: {numero_01}>{numero_02} = ", f"< Menor que: {numero_01}>{numero_02} = ", f"<= Menor o igual que: {numero_01}>{numero_02} = ", f"== Igual: {numero_01}>{numero_02} = ", f"!= Distinto: {numero_01}>{numero_02} = "]

# Lista 
resultado_comparacion = [mayor_que, mayor_igual_que, menor_que, menor_igual_que, igual, distinto]

for comparacion, resultado in zip(nombre_comparacion, resultado_comparacion):
    print(comparacion, resultado) 

