from virtualenv.util.zipapp import extract

menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

    elif opcao == "s":
        print("Saque")

    elif opcao == "e":
        print("Extrato")

    elif opcao == 'q':
        break;

    else:
        print("Operação inválida, selecione uma opção válida")




# Press the green button in the gutter to run the script.
#if __name__ == '__main__':



