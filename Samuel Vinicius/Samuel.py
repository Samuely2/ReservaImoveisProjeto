from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Criação do engine e da sessão
engine = create_engine('sqlite:///imoveis.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Definição da classe Proprietario
class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    imoveis = relationship("Imovel", back_populates="proprietario")

    def __repr__(self):
        return f'<Proprietario(nome={self.nome})>'

# Definição da classe Imovel
class Imovel(Base):
    __tablename__ = 'imoveis'

    id = Column(Integer, primary_key=True)
    endereco = Column(String)
    tipo = Column(String)
    preco = Column(Float)
    senha = Column(String)
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'))
    proprietario = relationship("Proprietario", back_populates="imoveis")

    def __repr__(self):
        return f'<Imovel(endereco={self.endereco}, tipo={self.tipo}, preco={self.preco}, senha={self.senha}, proprietario={self.proprietario.nome if self.proprietario else "N/A"})>'

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Operações CRUD

def criar_imovel(endereco, tipo, preco, nome_proprietario, senha):
    proprietario = session.query(Proprietario).filter_by(nome=nome_proprietario).first()
    if not proprietario:
        proprietario = Proprietario(nome=nome_proprietario)
        session.add(proprietario)
        session.commit()
    imovel = Imovel(endereco=endereco, tipo=tipo, preco=preco, senha=senha, proprietario=proprietario)
    session.add(imovel)
    session.commit()
    print("Imóvel criado com sucesso!")

def consultar_imovel(senha):
    imovel = session.query(Imovel).filter_by(senha=senha).first()
    if imovel:
        print(imovel)
    else:
        print("Imóvel não encontrado.")

def deletar_imovel(senha):
    imovel = session.query(Imovel).filter_by(senha=senha).first()
    if imovel:
        session.delete(imovel)
        session.commit()
        print("Imóvel deletado com sucesso!")
    else:
        print("Imóvel não encontrado.")

def main():
    while True:
        print('\nEscolha uma opção:')
        print('1. Criar Imóvel')
        print('2. Consultar Imóvel')
        print('3. Deletar Imóvel')
        print('4. Sair')

        opcao = input('Opção: ')
        if opcao == '1':
            endereco = input('Endereço do Imóvel: ')
            tipo = input('Tipo do Imóvel: ')
            preco = float(input('Preço do Imóvel: '))
            nome_proprietario = input('Nome do Proprietário do Imóvel: ')
            senha = input('Senha para o Imóvel: ')
            criar_imovel(endereco, tipo, preco, nome_proprietario, senha)
        elif opcao == '2':
            senha = input('Senha do Imóvel: ')
            consultar_imovel(senha)
        elif opcao == '3':
            senha = input('Senha do Imóvel a ser deletado: ')
            deletar_imovel(senha)
        elif opcao == '4':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
