#0123456789

nome = str(input('Digite seu nome:'))

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}*' 
    indice += 1

print(novo_nome)