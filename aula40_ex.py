''' calc with while '''

while True:
    print("\nSelecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("\nOpção inválida. Por favor, escolha uma operação válida.")
        continue

    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
    elif escolha == '2':
        resultado = num1 - num2
    elif escolha == '3':
        resultado = num1 * num2
    elif escolha == '4':
        if num2 == 0:
            print("Erro: Divisão por zero.")
            continue
        resultado = num1 / num2

    print("\nResultado: ", resultado)
    