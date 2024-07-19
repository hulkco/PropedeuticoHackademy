"""
    Ejemplos de uso de operadores en Python
    link: https://www.python.org/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

"""
    Operadores de Pertenencia en Python
    in
    not in   
"""
# Pertenencia

print("Operadores Pertenencia")
# Creamos una lista
colores = ["rojo","azul","verde","blanco","cafe"]
print("Contenido de la lista colores: ",colores)
print("Esta (in) 'azul' en 'colores'?","azul" in colores) # Devuelve True
print("Esta (in) 'violeta' en 'colores'?","violeta" in colores) # Devuelve False
print("No esta (not in) 'azul' en 'colores'?","azul" not in colores) # Devuelve False
print("No esta (not in) 'violeta' en colores","violeta" not in colores) # Devuelve True


