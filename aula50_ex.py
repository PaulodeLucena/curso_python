'''
Exercicio
Exiba os índices da lista
0 Mayara
1 Paulo
2 Oliver
'''

lista = ['Mayara', 'Paulo', 'Oliver']
lista.append('Lucena')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))