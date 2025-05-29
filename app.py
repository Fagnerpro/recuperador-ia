# app.py
import streamlit as st
from database import buscar_contexto
from llm_client import gerar_resposta

st.set_page_config(page_title="Recuperador IA", layout="wide")
st.title("🧠 Recuperação de Informação com LLM")

# Lista de perguntas sugeridas
sugestoes = [
    "O que é inteligência artificial?",
    "Qual a diferença entre IA e machine learning?",
    "Como os embeddings semânticos ajudam na busca por informações?",
    "Por que o MongoDB é indicado para dados não estruturados?",
    "Para que serve o Streamlit em ciência de dados?",
    "O que é recuperação de informação?",
    "Como funciona uma API de LLM como a OpenRouter?",
    "O que são embeddings em IA?",
    "Como a IA pode simular o comportamento humano?",
    "Qual o papel do Python na inteligência artificial?"
]

pergunta_sugerida = st.selectbox("💡 Ou escolha uma pergunta sugerida:", [""] + sugestoes)
pergunta_manual = st.text_input("Digite sua pergunta:")
pergunta = pergunta_manual if pergunta_manual else pergunta_sugerida

if 'historico' not in st.session_state:
    st.session_state.historico = []

# Botão para limpar histórico
if st.button("🧹 Limpar Histórico"):
    st.session_state.historico = []
    st.success("Histórico limpo com sucesso.")

if pergunta:
    with st.spinner("Consultando base de dados e gerando resposta..."):
        contexto = buscar_contexto(pergunta)
        resposta = gerar_resposta(pergunta, contexto)
        st.session_state.historico.append({"pergunta": pergunta, "resposta": resposta})

    st.subheader("Resposta da IA")
    st.write(resposta)
    st.download_button("📥 Copiar/Salvar Resposta", data=resposta, file_name="resposta.txt", mime="text/plain")

    if st.session_state.historico:
        historico_texto = "\n\n".join([
            f"🔹 Pergunta: {item['pergunta']}\nResposta: {item['resposta']}" for item in st.session_state.historico
        ])
        st.download_button("🗂️ Exportar Histórico", data=historico_texto, file_name="historico_ia.txt", mime="text/plain")

    with st.expander("📚 Contexto utilizado"):
        st.write(contexto)
