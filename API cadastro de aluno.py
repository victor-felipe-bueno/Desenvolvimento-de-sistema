from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="API de Cadastro de Alunos",
    description="API para realizar as quatro operações básicas (CRUD) para alunos.",
    version="1.0.0"
)

class Aluno(BaseModel):
    nome: str
    turma: str
    idade: int

db_alunos: Dict[int, Aluno] = {}

# --- ENDPOINTS DA API ---

@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "Bem-vindo à API de Cadastro de Alunos! Acesse /docs para a documentação interativa."}

@app.get("/alunos")
def listar_alunos():
    """Retorna todos os alunos cadastrados."""
    return db_alunos

@app.get("/alunos/{id}")
def pegar_aluno_por_id(id: int):
    """Retorna um aluno específico pelo seu Id (matrícula)."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    return db_alunos[id]

@app.post("/alunos/{id}", status_code=status.HTTP_201_CREATED)
def cadastrar_aluno(id: int, aluno: Aluno):
    """Cadastra um novo aluno com uma matrícula específica."""
    if id in db_alunos:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Aluno já cadastrado")
    
    db_alunos[id] = aluno
    return {"message": "Aluno cadastrado com sucesso!", "matricula": id, "aluno": aluno}

@app.put("/alunos/{id}")
def atualizar_aluno(id: int, aluno: Aluno):
    """Atualiza as informações de um aluno existente."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    
    db_alunos[id] = aluno
    return {"message": "Cadastro do aluno atualizado com sucesso!", "aluno": aluno}

@app.delete("/alunos/{id}")
def deletar_aluno(id: int):
    """Deleta o cadastro de um aluno."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    
    del db_alunos[id]
    return {"message": "Aluno deletado com sucesso!"}
