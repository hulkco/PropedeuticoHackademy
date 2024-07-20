"""
    Python
    link: https://www.python.org/
    Programa que:
    Crea un programa que reciba del usuario una frase y te diga si es o no palíndromo.
    Creado por: Gustavo Reynaga
    Julio del 2024
"""


def fraseEsPalindromo(frase):    
    frase =  frase.lower()  # Se convierte a minusculas
    frase = frase.replace(" ","") # se elimina los espacios en blanco
    # Se eliminan los acentos
    frase = frase.replace("á","a")
    frase = frase.replace("é","e")
    frase = frase.replace("í","i")
    frase = frase.replace("ó","o")
    frase = frase.replace("ú","u")

    # Variables de trabajo
    a = 0 # Indice de la Primer letra 
    b = len(frase) -1 # Se calcula el indice de la ultima letra

    # Ciclo for que verifica letra por letra
    for i in range(0, len(frase)):
        # Se comprueba que la letra en el indice 'a'
        # se igual al indice b
        if frase[a] == frase[b]:
            #Incrementamos en '1' para evaluar la siguiente letra 
            a += 1
            #Decrementamos en '1' para evaluar la siguiente letra 
            b -= 1
        #Si no hya coincidencia manda un False
        else:
            return False
    #Si hay coincidencia manda un True
    return True

frase=input("Ingresa una frase o palabra: ")

if fraseEsPalindromo(frase) == True:
    print("La frase/palabra es Palíndromo")
else:
    print("La frase/palabra no es Palíndromo")