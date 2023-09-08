"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Digite o horário atual: ')
minutos = int(input('Quantos minutos: '))

# PODE HAVER UM ERRO CASO SEJA COLOCADO FLOAT EM VEZ DE INT, MELHOR OPÇÃO É TRY/EXCEPT
if horario.isdigit():
    horario_int = int(horario)

if 0 <= horario_int < 12:
    print(f"Bom dia, o horário atual é: {horario_int}:{minutos}")
elif 12 <= horario_int < 18:
    print(f"Boa tarde, o horário atual é: {horario_int}:{minutos}")
elif 18 <= horario_int <= 23:
    print(f'Boa noite, o horário atual é: {horario_int}:{minutos}')  
else: 
    print('Não conheço esse horário, coloque um horário valido')

# MELHOR OPÇÃO 

try:
    if horario.isdigit():
        horario_int = int(horario)

    if 0 <= horario_int < 12:
        print(f"Bom dia, o horário atual é: {horario_int}:{minutos}")
    elif 12 <= horario_int < 18:
        print(f"Boa tarde, o horário atual é: {horario_int}:{minutos}")
    elif 18 <= horario_int < 24:
        print(f'Boa noite, o horário atual é: {horario_int}:{minutos}')  
    else: 
        print('Não conheço esse horário, coloque um horário valido')
except:
    print('Por favor, digite apenas numeros inteiros.')
