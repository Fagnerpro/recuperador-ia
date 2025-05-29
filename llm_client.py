# llm_client.py
import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def gerar_resposta(pergunta, contexto):
    if not API_KEY:
        return "🔒 A variável OPENROUTER_API_KEY não foi carregada corretamente. Verifique os 'Secrets' no Streamlit Cloud."

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

    try:
        response = requests.post(API_URL, headers=headers, json=body, timeout=15)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        elif response.status_code == 401:
            return "❌ Erro 401: A chave da OpenRouter é inválida ou foi rejeitada. Verifique os secrets."
        elif response.status_code == 403:
            return "❌ Erro 403: Acesso proibido à API. Verifique permissões da chave."
        else:
            return f"⚠️ Erro {response.status_code}: A API retornou uma falha inesperada."
    except Exception as e:
        return f"⚠️ Falha ao conectar com a API da OpenRouter. Simulando resposta...\n\n🤖 Pergunta: {pergunta}\n📚 Contexto usado: {contexto[:150]}...\n\n💡 Resposta simulada: Este é um exemplo de resposta gerada sem conexão com a LLM."
