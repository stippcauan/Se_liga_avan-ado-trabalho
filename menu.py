def calcular_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual= int(input("Digite que dia é hoje"))
    idade = ano_atual - ano_nascimento

    print(f"Você tem {idade} anos.")

def calcular_compra():
    total = 0
    while True:
        preco_item = float(input("digite"))

def calcular_preco_compra():
    
    total = 0
    while True:
        try:
            preco_str = input("Digite o preço do item (ou 'f' para finalizar): R$ ")
            if preco_str.lower() == 'f':
                break
            preco = float(preco_str)
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            total += preco
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um preço válido ou 'f' para finalizar.\n")
    print(f"\nO preço total da compra é: R$ {total:.2f}\n")


def menu_principal():



opcao = input("Escolha uma opção: ")

print("")
print("(1)-calcular_idade (2)- calcular_preço_da _compra (3)- sair ")
print("")
nível = int(input("Escolha um nível"))

if (nível == 1): 
    calcular_idade()
elif (nível == 2): 
    calcular_preco_compra()
elif (nível == 3): 
    print("Saindo do programa. Até mais!")
    break
else:
print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.\n")

if __name__ == "__main__":
    menu_principal()