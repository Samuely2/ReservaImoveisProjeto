from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# aqui eu criei a classe proprietario onde vai ficar as informações do mesmo
class Proprietario(Base):
    __tablename__ = 'proprietarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    imoveis = relationship("Imovel", back_populates="proprietario")

# aqui eu criei a classe imovel onde vai ficar as informações do imovel
class Imovel(Base):
    __tablename__ = 'imoveis'
    id = Column(Integer, primary_key=True)
    endereco = Column(String, nullable=False)
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'))
    proprietario = relationship("Proprietario", back_populates="imoveis")
    locacoes = relationship("Locacao", back_populates="imovel")

# e por ultimo aqui é onde eu criei a classe da locação onde vai ter as informações da locação do imovel
class Locacao(Base):
    __tablename__ = 'locacoes'
    id = Column(Integer, primary_key=True)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)
    imovel_id = Column(Integer, ForeignKey('imoveis.id'))
    imovel = relationship("Imovel", back_populates="locacoes")

# aqui é onde configura a engine e cria as tabelas
engine = create_engine('sqlite:///imobiliaria.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
