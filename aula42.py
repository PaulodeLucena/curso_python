frase = 'O Python é uma linguagem de programação multiparadigma. Foi criado por Gui van Rossum'


i = 0

apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i <len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':

        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}", {apareceu_mais_vezes} vezes')