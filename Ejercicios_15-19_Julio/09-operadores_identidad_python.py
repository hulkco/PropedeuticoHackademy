"""
    Ejemplos de uso de operadores en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Operadores de Identidad en Python  
"""
# Identidad

print("Operadores de Identidad")

a = 3
b = 3  
c = 4
print("Se tiene las siguientes variables: a=3, b=3, c=3")
print("Se muestra la direccion en memoria de cada variable: ")
# la funcion id(), muestra la direccion en memoria del objeto
print("Direccion de a:",id(a)) 
print("Direccion de b:",id(b))
print("Direccion de c:",id(c))
is_operando = a is b
print ("Operando is: a is b",is_operando) # muestra True
is_not_operando = a is not b
print ("Operando is not: a is not b", is_not_operando) # muestra False
is_not_operando = a is not c
print ("Operando is not: a is not c", is_not_operando) # muestra True

