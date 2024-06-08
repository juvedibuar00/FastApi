from fastapi import FastAPI
from pydantic import BaseModel
class Produto(BaseModel):
    nome:str
    preco: float

bancoDados = {
    "1": {
        "nome": "Pizza",
        "preco": 59.90
    },
    "2":{
        "nome": "Lisanha",
        "preco": 9.90
    },
    "3": "Batata-doce",
    "preco": 2.5
}





app = FastAPI()
#rota prinpicipal de apresentação

@app.get("/")
def apresentacao():
    return {
        "mensagem": "Olá, mundo",
        "statusCode": 200
    }

@app.get("/{nome}")
def saudacao(nome):
    return {
        "mensagem": f"Olá, {nome}",
        "statusCode": 200
    }


@app.get("/produtos/")
def mostrarTodosProdutos():
    return bancoDados

@app.get("/produtos/{idProdutos}")
def mostrarUmProduto(idProduto):
    try:
        if bancoDados[idProduto]:
            return {
                "produto": bancoDados[idProduto],
                "statusCode": 200
            }

    except:
            return {
                "produto": "Não encontrado",
                "statusCode": 404
            }


@app.post("/produtos/cadastrar/")
def cadastrarProduto(id:int, item: Produto):
    listaProdutos = print(bancoDados.values())
    for produto in listaProdutos:
        if produto['nome'] == item.nome:
            return {
                "mensagem": "Produto já cadastro",
                "statusCode": 400
            }
        else:

            bancoDados[id]= item
            return {
                "Mensagem": " Item criado com sucesso",
                "Produto": item,
                "statusCode": 200
            }


@app.delete(f"/produtos/excluir/{id}")
def excluirProduto(id:int):
    del bancoDados[id]
    return {
        "mensagem":"Produto excluído",
        "idProduto": id,
        "statusCode": 200
    }