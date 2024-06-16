from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria uma base declarativa
Base = declarative_base()

# Define a classe Cartoes que representa a tabela cartoes
class Cartao(Base):
    __tablename__ = 'cartoes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    banco = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    limite = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)

# Cria uma engine SQLite (o arquivo example.db será criado ou usado se já existir)
engine = create_engine('sqlite:///financial_control.db')

# Cria todas as tabelas
Base.metadata.create_all(engine)

# Cria uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adiciona alguns cartões como exemplo
cartao1 = Cartao(banco="Banco A", nome="Cartão A", limite=5000.00, tipo="Crédito")
cartao2 = Cartao(banco="Banco B", nome="Cartão B", limite=3000.00, tipo="Débito")

# Adiciona os cartões na sessão
session.add(cartao1)
session.add(cartao2)

# Salva as alterações
session.commit()

# Consulta todos os cartões
cartoes = session.query(Cartao).all()
for cartao in cartoes:
    print(cartao.id, cartao.banco, cartao.nome, cartao.limite, cartao.tipo)

# Fecha a sessão
session.close()
