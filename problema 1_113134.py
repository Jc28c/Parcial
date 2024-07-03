#Problema 1: Palabras palindromas
palabra = input('Ingrese la palabra a verificar: ')
verificacion = ''
for i in palabra:
    verificacion = i + verificacion
if palabra == verificacion:
    print(f'La palabra {palabra} es palindroma')
else:
    print(f'La palabra {palabra} no es palindroma')