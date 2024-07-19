"""
    Ejemplos de uso de operadores en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Operadores Aritméticos en Python        
"""
# Aritméticos
numero_01 = 15
numero_02 = 4

suma = numero_01 + numero_02
resta = numero_01 - numero_02
multiplicacion = numero_01 * numero_02
division = numero_01 / numero_02
modulo = numero_01 % numero_02
potencia = numero_02 ** numero_02
div_entero = numero_01 // numero_02

print("Operadores Aritméticos")
"""
    Se crean dos listas, la primera contiene el titulo de la operacion aritmetica y la segunda el resultado
"""
# Lista titulos
nombre_operacion = [f"Suma: {numero_01}+{numero_02}= ", f"Resta: {numero_01}-{numero_02}= ", f"Multiplicación: {numero_01}*{numero_02}= ",f"División: {numero_01}+{numero_02}= ", f"Modulo: {numero_01}%{numero_02}= ", f"Potencia: {numero_01}**{numero_02}= ", f"División entero {numero_01}//{numero_02}= " ]
# Lista resultados
resultado_operacion = [suma, resta, multiplicacion, division, modulo, potencia, div_entero]

"""
    Se crea un bucle for con la funcion zip, para iterar con las
    dos listas anteriores y imprimir en consola el resultado
"""

for operacion, resultado in zip(nombre_operacion, resultado_operacion):
    print(operacion, resultado)

