# 💡 Recuperador IA

Aplicação desenvolvida com **Streamlit**, **MongoDB** e **OpenRouter API** para responder perguntas com base em dados armazenados. Projeto da disciplina **IA Aplicada à Recuperação de Informação** — SENAI.

![Interface](https://raw.githubusercontent.com/Fagnerpro/recuperador-ia/main/assets/print_interface.png)

---

## 🚀 Funcionalidades

- Entrada de pergunta manual ou seleção sugerida
- Busca de contexto em MongoDB Atlas com regex
- Envio de pergunta + contexto à LLM via OpenRouter
- Geração de resposta textual em linguagem natural
- Visualização do contexto utilizado
- 📥 Botão para baixar resposta individual
- 🗂️ Exportação do histórico completo de interações
- 🧹 Botão para limpar histórico de sessão
- 🔁 Resposta simulada se a API falhar

---

## 🧰 Tecnologias Utilizadas

| Ferramenta | Finalidade |
|-----------|------------|
| Streamlit | Interface web |
| MongoDB Atlas | Base de dados NoSQL |
| OpenRouter API | Acesso a modelo LLM (Mistral-7B) |
| Python | Lógica e integração |

---

## 📦 Instalação Local

```bash
git clone https://github.com/Fagnerpro/recuperador-ia.git
cd recuperador-ia
pip install -r requirements.txt
```

Crie um arquivo `.env`:

```env
MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster.mongodb.net/?retryWrites=true&w=majority
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Execute o app:
```bash
streamlit run app.py
```

---

## ☁️ Deploy no Streamlit Cloud

1. Acesse https://streamlit.io/cloud e conecte ao GitHub
2. Crie novo app apontando para `Fagnerpro/recuperador-ia`, branch `main`, arquivo `app.py`
3. Vá em **Settings > Secrets** e configure:

```toml
MONGO_URI = "sua_string_de_conexao"
OPENROUTER_API_KEY = "sua_chave_openrouter"
```

---

## 📄 Licença

Projeto de uso educacional, distribuído livremente para fins de aprendizagem e demonstração técnica.
