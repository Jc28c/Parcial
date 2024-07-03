#Problema 2: Anagramas
palabra_1 = list(input('Ingresa la primera palabra: '))
palabra_2 = list(input('Ingresa la segunda palabra: '))
verificacion_1 = []
verificacion_2 = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in palabra_1:
    for j in abc:
        if i == j:
            verificacion_1.append(j)
print(verificacion_1)
for i in palabra_1:
    for j in palabra_2:
        if i == j:
            