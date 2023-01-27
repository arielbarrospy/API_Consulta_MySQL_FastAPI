from fastapi import APIRouter, HTTPException, status, Depends
from src.infra.sqlalchemy.configs.config import get_db
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.repo_consulta import RepositorioConsulta
from src.schemas.schema import Entrada


router = APIRouter()




@router.post('/cnpj/')
def consulta(consulta:Entrada,session: Session = Depends(get_db)):
    cnpj = consulta.cnpj
    consulta = RepositorioConsulta(session).primeiro(cnpj)
    print(consulta)