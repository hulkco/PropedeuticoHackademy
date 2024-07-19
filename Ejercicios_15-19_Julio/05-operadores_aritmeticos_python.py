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
suma = 12 + 4
resta = 12 - 4
multiplicacion = 12 * 4
division = 12 / 5
modulo = 18 % 3
potencia = 12 ** 4
div_entero = 12 // 5

print("Operadores Aritméticos")

"""
    Se crean dos listas, la primera contiene el titulo de la operacion aritmetica y la segunda el resultado
"""
# Lista titulos
nombre_operacion = ["Suma: ", "Resta: ", "Multiplicación: ","División: ", "Modulo: ", "Potencia: ", "División entero" ]
# Lista resultados
resultado_operacion = [suma, resta, multiplicacion, division, modulo, potencia, div_entero]

"""
    Se crea un bucle for con la funcion zip, para iterar con las
    dos listas anteriores y imprimir en consola el resultado
"""
for operacion, resultado in zip(nombre_operacion, resultado_operacion):
    print(operacion, resultado)

