# aqui criei uma função pro CRUD, o menu das opções que o cliente pode escolher
def menu():
    while True:
        print("\nSistema de Gerenciamento de Imobiliária")
        print("1. Adicionar Proprietário")
        print("2. Adicionar Imóvel")
        print("3. Adicionar Locação")
        print("4. Listar Proprietários")
        print("5. Listar Imóveis")
        print("6. Listar Locações")
        print("7. Excluir Imóvel")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do Proprietário: ")
            adicionar_proprietario(nome)
        elif escolha == '2':
            endereco = input("Endereço do Imóvel: ")
            proprietario_id = int(input("ID do Proprietário: "))
            adicionar_imovel(endereco, proprietario_id)
        elif escolha == '3':
            data_inicio = input("Data de Início da Locação (YYYY-MM-DD): ")
            imovel_id = int(input("ID do Imóvel: "))
            adicionar_locacao(data_inicio, imovel_id)
        elif escolha == '4':
            listar_proprietarios()
        elif escolha == '5':
            listar_imoveis()
        elif escolha == '6':
            listar_locacoes()
        elif escolha == '7':
            imovel_id = int(input("ID do Imóvel a ser Excluído: "))
            excluir_imovel(imovel_id)
        elif escolha == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
