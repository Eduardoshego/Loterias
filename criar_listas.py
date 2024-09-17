import random as rd

def criar_lista_de_numeros(qdt_numeros, range_numeros):
    lista_de_numeros_sorteados = []
    for c in range(0, qdt_numeros):
        while True:
            numero_sorteado = rd.randint(1, range_numeros + 1)
            if numero_sorteado not in lista_de_numeros_sorteados:
                lista_de_numeros_sorteados.append(numero_sorteado)
                break
       
            
    return lista_de_numeros_sorteados

def criar_lista_ordenada(lista):
    return sorted(lista)
# Testando a função


lista1 = criar_lista_de_numeros(6, 60)
lista2 = criar_lista_ordenada(lista1)
print(lista1)
print(lista2)
