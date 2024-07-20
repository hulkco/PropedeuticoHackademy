"""
    Ejemplos de uso de Excepciones en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Excepciones en Python   
    
"""
print("Control de errores con excepciones en Python")
print("\nPython permite manejar las excepciones de manera generica con\nel uso de la clase 'Exception'\n")
print("Ejemplo 1: Usaremos el error clasico de dividir entre cero.\nSi intentamos ejecutar el siguiente codigo: \n")
print('print(1/0)\n')
print("Se mostrara el siguiente error:\n")
print("16-excepciones.py, line 16, in <module>\n    print(1/0)\n          ~^~\nZeroDivisionError: division by zero")
print("1/0")
print("\nPara evitar el error anterior, usaremos 'try' y 'except'\n")
print('try:\n    print(1/0)\nexcept Exception:\n    print("Hay un error el codigo, favor de revisar")\n')
print("Resultado: \n")

try:
    print(1/0)
except Exception:
    print("Hay un error el codigo, favor de revisar\n")

print("Ejemplo 2: Si deseamos que se muestre que excepcion ha ocurrido, se utiliza\n'as ex' y 'type(ex)'\n")
print('try:\n    print(1/0)\nexcept Exception as ex:\n    print("Hay un error el codigo, favor de revisar", type(ex))\n')
print("Resultado: \n")

try:
    print(1/0)
except Exception as ex:
    print("Hay un error el codigo, favor de revisar", type(ex))
