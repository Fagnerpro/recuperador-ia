from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["base_ia"]
colecao = db["documentos"]

def buscar_contexto(pergunta):
    try:
        resultados = colecao.find({"conteudo": {"$regex": pergunta, "$options": "i"}}).limit(3)
        contexto = "\n\n".join([doc["conteudo"] for doc in resultados])
        return contexto if contexto else "Nenhum contexto encontrado na base."
    except ConnectionFailure:
        return "Erro ao conectar com o banco de dados."

