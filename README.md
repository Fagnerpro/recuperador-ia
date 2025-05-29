# README.md

## 💡 Recuperador IA — Projeto Final SENAI

Este projeto implementa uma aplicação de recuperação de informações utilizando **Streamlit**, **MongoDB** e uma **LLM via OpenRouter.ai**.

---

### 🚀 Funcionalidades
- Entrada de pergunta via interface web
- Consulta à base de dados NoSQL (MongoDB)
- Envio de pergunta + contexto para uma LLM
- Exibição da resposta gerada pela IA

---

### 🧰 Tecnologias Utilizadas
- Python + Streamlit
- MongoDB Atlas
- OpenRouter (modelo mistralai/mistral-7b-instruct)

---

### 📦 Instalação Local

1. Clone este repositório
```bash
git clone https://github.com/seuusuario/recuperador-ia.git
cd recuperador-ia
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente
Crie um arquivo `.env` com o conteúdo:
```env
OPENROUTER_API_KEY=sua_chave_api_aqui
```

4. Rode a aplicação
```bash
streamlit run app.py
```

---

### 🌐 MongoDB Atlas
- Crie uma base chamada `base_ia` com a coleção `documentos`
- Importe o arquivo `dataset_exemplo.json`

---

### 🌍 OpenRouter
- Crie uma conta gratuita em https://openrouter.ai
- Copie sua chave de API e insira no `.env`

---

### 📄 Licença
Este projeto é livre para fins educacionais. Desenvolvido como parte do curso **IA Aplicada à Recuperação de Informação — SENAI Goiás**.