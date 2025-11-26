import datetime

def calcular_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite que ano nós estamos"))
    idade = ano_atual - ano_nascimento
 
    print(f"Você tem {idade} anos.")


def calcular_preco_compra():
    total = 0.0
    while True:
        try:
            preco_str = input("Digite o preço do item (ou '4' para finalizar): ")
            if preco_str.lower() == '4':
                break
            preco = float(preco_str)
            total += preco
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou '4'.")
    print(f"\nO preço total da compra é: R$ {total:.2f}.\n")

def menu_principal():
    while True:
        print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
        print("🟩    MENU DO PROGRAMA   I")
        print("🟩           DO          I")
        print("🟩         CAUAN         I")
        print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

        opcao = input("Escolha uma opcao (1, 2 ou 3):")


        print("(1)-calcular_idade (2)- calcular_preco_da_compra (3)- sair ")
       

        if opcao == '1':
            calcular_idade()
        elif opcao == '2':
            calcular_preco_compra()
        elif opcao == '3':
            print("sair do programa")
            break
        else:
            print("\nOpção invalida. por favor escolha 1, 2 ou 3.\n")
           
if __name__=="__main__":
    menu_principal()