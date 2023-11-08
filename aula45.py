"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for item in texto
texto = 'farofa' #iterável
# iteratador = iter(texto) #iterator

# while True:
#     try:            
#         print(next(iteratador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)