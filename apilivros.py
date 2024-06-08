from fastapi import  FastAPI
from  pydantic import BaseModel

bdLivros = {}
class Livro (BaseModel):
    #dentro da classe BaseModel não se usa vírgula
    id: int
    titulo: str
    autor: str
    ano: int
    preco: float
    disponibilidade: bool

#ANTES DE INICIAR O METODO
app = FastAPI()
@app.get("/")
def mostrarInfos():
    return {
        "mensagem": "Api de livros",
        "versão": "1.0"
    }

@app.get("/livros/")
def mostrarTodosLivros():
    return {
        "Livro": bdLivros,
        "statusCode": 200
    }

@app.get("/Livros/{id}")
def mostrarUmLivro(id: int):
   try:
        return {
            "Livro": bdLivros,
            "statusCode": 200
        }
   except
   return {
       "Livro": "Não encontrado",
       "statusCode": 404
   }