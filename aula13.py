nome = str(input("Digite seu nome:"))
peso = int(input("Digite seu peso:"))
altura_em_metros = float(input("Digite sua altura (em metros):"))
imc = peso / altura_em_metros ** 2


print(f'{nome} tem {altura_em_metros} de altura e pesa {peso}')
print(f'Seu imc é {imc:.2f}')