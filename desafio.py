# desafio criar sistema bancario

menu = """
==========================
Bem-vindo ao Banco Python
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
==========================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
        else:
            print("Operacao falhou! O valor informado e invalido.")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente.")
        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operacao falhou! O valor informado e invalido.")
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    elif opcao == "0":
        print("Obrigado por utilizar o Banco Python. Ate mais!")
        break
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")