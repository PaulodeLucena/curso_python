# text = 'Python s2'

# i = 0
# tamanho_string = len(text)

# while i < tamanho_string:
#     print(text[i], i )

#     i += 1

text = 'Python'

novo_texto = ''

for letra in text:
    novo_texto += f"*{letra}"
    print(letra)
print(novo_texto)