from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

# Classe Proprietario
class Proprietario(Base):
    __tablename__ = 'proprietarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    imoveis = relationship("Imovel", back_populates="proprietario")

# Classe Imovel
class Imovel(Base):
    __tablename__ = 'imoveis'
    id = Column(Integer, primary_key=True)
    endereco = Column(String, nullable=False)
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'))
    proprietario = relationship("Proprietario", back_populates="imoveis")
    locacoes = relationship("Locacao", back_populates="imovel")

# Classe Locacao
class Locacao(Base):
    __tablename__ = 'locacoes'
    id = Column(Integer, primary_key=True)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)
    imovel_id = Column(Integer, ForeignKey('imoveis.id'))
    imovel = relationship("Imovel", back_populates="locacoes")

# Configuração da engine e criação das tabelas
engine = create_engine('sqlite:///imobiliaria.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def imprimir_imoveis_impacta():
    print("""

██╗███╗░░░███╗██████╗░░█████╗░░█████╗░████████╗░█████╗░  ██╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗██╗░██████╗
██║████╗░████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██║████╗░████║██╔══██╗██║░░░██║██╔════╝██║██╔════╝
██║██╔████╔██║██████╔╝███████║██║░░╚═╝░░░██║░░░███████║  ██║██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░██║╚█████╗░
██║██║╚██╔╝██║██╔═══╝░██╔══██║██║░░██╗░░░██║░░░██╔══██║  ██║██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░██║░╚═══██╗
██║██║░╚═╝░██║██║░░░░░██║░░██║╚█████╔╝░░░██║░░░██║░░██║  ██║██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗██║██████╔╝
╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝╚═════╝░
          """)

def adicionar_proprietario(nome):
    try:
        proprietario = Proprietario(nome=nome)
        session.add(proprietario)
        session.commit()
        print('*****************')
        print(f'Proprietário {nome} adicionado com sucesso!')
        print('*****************')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar proprietário: {e}')

def adicionar_imovel(endereco, proprietario_id):
    try:
        proprietario = session.query(Proprietario).filter_by(id=proprietario_id).one()
        imovel = Imovel(endereco=endereco, proprietario=proprietario)
        session.add(imovel)
        session.commit()
        print('*****************')
        print(f'Imóvel no endereço {endereco} adicionado com sucesso!')
        print('*****************')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar imóvel: {e}')

def adicionar_locacao(data_inicio, imovel_id):
    try:
        imovel = session.query(Imovel).filter_by(id=imovel_id).one()
        locacao = Locacao(data_inicio=datetime.strptime(data_inicio, '%Y-%m-%d'), imovel=imovel)
        session.add(locacao)
        session.commit()
        print('*****************')
        print(f'Locação para o imóvel {imovel.endereco} adicionada com sucesso!')
        print('*****************')
    except Exception as e:
        session.rollback()
        print(f'Erro ao adicionar locação: {e}')

def listar_proprietarios():
    proprietarios = session.query(Proprietario).all()
    for proprietario in proprietarios:
        print('*****************')
        print(f'ID: {proprietario.id}, Nome: {proprietario.nome}')
        print('*****************')

def listar_imoveis():
    imoveis = session.query(Imovel).all()
    for imovel in imoveis:
        print('*****************')
        print(f'ID: {imovel.id}, Endereço: {imovel.endereco}, Proprietário: {imovel.proprietario.nome}')
        print('*****************')

def listar_locacoes():
    locacoes = session.query(Locacao).all()
    for locacao in locacoes:
        print(f'ID: {locacao.id}, Início: {locacao.data_inicio}, Fim: {locacao.data_fim}, Imóvel: {locacao.imovel.endereco}')

def excluir_imovel(imovel_id):
    try:
        imovel = session.query(Imovel).filter_by(id=imovel_id).one()
        session.delete(imovel)
        session.commit()
        print('*****************')
        print(f'Imóvel {imovel.endereco} excluído com sucesso!')
        print('*****************')
    except Exception as e:
        session.rollback()
        print(f'Erro ao excluir imóvel: {e}')

def menu():
    while True:
        imprimir_imoveis_impacta()  # Aqui é onde a função é chamada
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
        print('-----------------------------')

        if escolha == '1':
            nome = input("Nome do Proprietário: ")
            print('-----------------------------')
            adicionar_proprietario(nome)
        elif escolha == '2':
            endereco = input("Endereço do Imóvel: ")
            print('-----------------------------')
            proprietario_id = int(input("ID do Proprietário: "))
            print('-----------------------------')
            adicionar_imovel(endereco, proprietario_id)
        elif escolha == '3':
            data_inicio = input("Data de Início da Locação (YYYY-MM-DD): ")
            print('-----------------------------')
            imovel_id = int(input("ID do Imóvel: "))
            print('-----------------------------')
            adicionar_locacao(data_inicio, imovel_id)
        elif escolha == '4':
            listar_proprietarios()
        elif escolha == '5':
            listar_imoveis()
        elif escolha == '6':
            listar_locacoes()
        elif escolha == '7':
            imovel_id = int(input("ID do Imóvel a ser Excluído: "))
            print('-----------------------------')
            excluir_imovel(imovel_id)
        elif escolha == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")
            print('-----------------------------')

if __name__ == "__main__":
    menu()