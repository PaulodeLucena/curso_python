"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Digite o primeiro nome do usuário: '))
tamanho_nome = len(nome)

if 1 <= tamanho_nome <= 4:
    print('Seu nome é muito pequeno')
elif 5 <= tamanho_nome <= 6:
    print('Seu nome é normal')
elif tamanho_nome > 6:
    print('Seu nome é muito grande')
else: 
    print('Você digitou um caracter invalido ou digitou vazio, por gentileza, escreva ao menos uma letra')