"""
    Ejemplos de uso de operadores en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Operadores Bitwise en Python
    & and
    | or
    ^ xor
    ~ NOT
    >> Desplaza a la derecha
    << Desplaza a la izquierda
"""
# Bitwise
valor1 = 2
valor2 = 3

print("Operadores Bitwise (bit a bit)")

print(f"Tenemos a valor1=4 (en binario = {bin(valor1)}) y valor2=6 (en binario = {bin(valor2)}) ")

print("Operador & and")
print("valor1 & valor2=",bin(valor1 & valor2),"<= En binario")

print("Operador | or")
print("valor1 | valor2=",bin(valor1 | valor2),"<= En binario")

print("Operador ^ xor")
print("valor1 ^ valor2=",bin(valor1 ^ valor2),"<= En binario")

print("Operador ~ NOT")
print("~valor1=",bin(~valor1),"<= En binario")

print("Operador >>")
print("valor1 >> valor2=",bin(valor1 >> valor2),"<= En binario")
#
print("Operador <<")
print("valor1 << valor2=",bin(valor1 << valor2),"<= En binario")
#

