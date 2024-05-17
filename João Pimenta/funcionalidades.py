from datetime import datetime

# criei uma função que adiciona o proprietario
def adicionar_proprietario(nome):
    try:
        proprietario = Proprietario(nome=nome)
        session.add(proprietario)
        session.commit()
        print(f'Proprietário {nome} adicionado com sucesso!')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar proprietário: {e}')

# função que cria adiciona o imóvel
def adicionar_imovel(endereco, proprietario_id):
    try:
        proprietario = session.query(Proprietario).filter_by(id=proprietario_id).one()
        imovel = Imovel(endereco=endereco, proprietario=proprietario)
        session.add(imovel)
        session.commit()
        print(f'Imóvel no endereço {endereco} adicionado com sucesso!')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar imóvel: {e}')

#  essa função adiciona a locação
def adicionar_locacao(data_inicio, imovel_id):
    try:
        imovel = session.query(Imovel).filter_by(id=imovel_id).one()
        locacao = Locacao(data_inicio=datetime.strptime(data_inicio, '%Y-%m-%d'), imovel=imovel)
        session.add(locacao)
        session.commit()
        print(f'Locação para o imóvel {imovel.endereco} adicionada com sucesso!')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar locação: {e}')

# função que lista os proprietarios do imóvel
def listar_proprietarios():
    proprietarios = session.query(Proprietario).all()
    for proprietario in proprietarios:
        print(f'ID: {proprietario.id}, Nome: {proprietario.nome}')

# função que lista os imóveis
def listar_imoveis():
    imoveis = session.query(Imovel).all()
    for imovel in imoveis:
        print(f'ID: {imovel.id}, Endereço: {imovel.endereco}, Proprietário: {imovel.proprietario.nome}')

# lista as locações
def listar_locacoes():
    locacoes = session.query(Locacao).all()
    for locacao in locacoes:
        print(f'ID: {locacao.id}, Início: {locacao.data_inicio}, Fim: {locacao.data_fim}, Imóvel: {locacao.imovel.endereco}')

# função que exclui o imóvel
def excluir_imovel(imovel_id):
    try:
        imovel = session.query(Imovel).filter_by(id=imovel_id).one()
        session.delete(imovel)
        session.commit()
        print(f'Imóvel {imovel.endereco} excluído com sucesso!')
    except Exception as e:
        session.rollback()
        print(f'Erro ao excluir imóvel: {e}')
