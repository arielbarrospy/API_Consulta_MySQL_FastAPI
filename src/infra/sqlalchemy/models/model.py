from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.configs.config import Base


class Entrada(Base):
    __tablename__ ="estabelecimentos"
    cnpj = Column(Integer),
    razao_social = Column(String),
    nome_fantasia = Column(String),
    nome_socio = Column(String),
    atividade_principal = Column(String),
    natureza_juridica = Column(String),
    estado = Column(String),
    municipio = Column(String),
    bairro = Column(String),
    cep = Column(String),
    ddd = Column(String),
    data_abertura = Column(String),
    data_abertura2 = Column(String),
    capital_social = Column(String),
    capital_social2 = Column(String)