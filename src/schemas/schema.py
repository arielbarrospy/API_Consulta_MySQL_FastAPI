from pydantic import BaseModel
from typing import List, Optional




class Entrada(BaseModel):
    cnpj: Optional[str] = '',
    razao_social: Optional[str] = '',
    nome_fantasia: Optional[str] = '',
    nome_socio: Optional[str] = '',
    atividade_principal: Optional[str] = '',
    natureza_juridica: Optional[str] = '',
    estado: Optional[str] = '',
    municipio: Optional[str] = '',
    bairro: Optional[str] = '',
    cep: Optional[str] = '',
    ddd: Optional[str] = '',
    data_abertura: Optional[str] = '',
    data_abertura2: Optional[str] = '',
    capital_social: Optional[str] = '',
    capital_social2: Optional[str] = ''
    
    class Config:
        orm_mode = True
        