qnt_entradas = int(input(""))

raw_numeros = []

for i in range(qnt_entradas):
    raw_numeros.append(int(input()))

count = {}

numeros = []

for i in raw_numeros:
    if not i in count:
        count[i] = 1
        numeros.append(i)
    else:
        count[i] += 1


len_numeros = len(numeros)

estaOrdenado = False
while not estaOrdenado:
    estaOrdenado = True
    for i in range(len_numeros):
        numero = numeros[i]

        if i < len_numeros-1:
            numero_next = numeros[i+1]

            if numero > numero_next:
                estaOrdenado = False
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]

for n in numeros:
    print(f"{n} aparece {count[n]} vez(es)")


'''
    VERSAO DE PREGUIÇOSO
'''

qnt_entradas = int(input(""))

numeros = []

for i in range(qnt_entradas):
    numeros.append(int(input()))

numeros.sort()
repetidos = []
for i in numeros:
    if i not in repetidos:
        print(f"{i} aparece {numeros.count(i)} vez(es)")
        repetidos.append(i)
