"""
    Python
    link: https://www.python.org/
    Programa que:
    Crea un programa que reciba del usuario una palabra o frase y la transforme a lenguaje leet, puedes revisar esta guía https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
    Creado por: Gustavo Reynaga
    Julio del 2024
"""

# Ya no me alcanzo el tiempo para capturar todo el abecedario

texto = input('Ingresa texto a convertir: ')

for char in texto:
	if char == 'a':
		texto = texto.replace('a','4')
	elif char == 'b':
		texto = texto.replace('b','8')
	elif char == 'e':
		texto = texto.replace('e','3')
	elif char == 'l':
		texto = texto.replace('l','1')
	elif char == 'o':
		texto = texto.replace('o','0')
	elif char == 's': 
		texto = texto.replace('s','5')
	elif char == 't':
		texto = texto.replace('t','7')
	else:
		pass

print(texto)