# llm_client.py
import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def gerar_resposta(pergunta, contexto):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Você é um assistente especializado em responder perguntas com base em contexto fornecido."},
            {"role": "user", "content": f"Contexto: {contexto}\n\nPergunta: {pergunta}"}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro na resposta da LLM: {response.status_code}"
