menu = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
ls = 3
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Digite o valor a ser depositado: '))

        if valor > 0:
            saldo = saldo + valor
            extrato += f'Deposito: R${valor:.2f}\n'
            print('Valor Depositado')

        else:
            print('Valores negativos não são permitidos. ')

    elif opcao == "s":
        valor = float(input('Informe o valor que deseja sacar: '))
        fora_limite = valor > limite
        sem_saldo = valor > saldo
        qtd_saque = numero_saques >= ls

        if fora_limite:
            print('Operação falhou! O valor do saque está acima do valor limite por saque')

        elif sem_saldo:
            print('Operação falou! Saldo insifucuente')

        elif qtd_saque:
            print('Operação falhou! Linte de quantidade de saques excedida')

        elif valor > 0:
            saldo = saldo - valor
            extrato += f' Saque: R${valor:.2f}\n'
            numero_saques = numero_saques + 1
            print(f'Sacado valor de R${valor:.2f}')
            
        else:
            print('Operação falhoou, o valor informado é inválido')
      

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print('Não foram realizadas transações. ' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')
        print('=================================')

    elif opcao == "q":
        break

    else:
        print('Opreação inválida, por favor digite a opção desejada')