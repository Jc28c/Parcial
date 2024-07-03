#Problema 3: Codificacion con primos
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
primos = []
contador_de_primos = 0
for i in range(2,400):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        primos.append(i)
        contador_de_primos += 1
    if contador_de_primos == 27:
        break
print(primos)
clave = int(input('Ingresa el numero de cifrado: '))
while True:
    for i in range(primos + 1):
        for j in range(len(abc) + 1):
            if i == abc[j]:
                