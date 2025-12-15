# 🤖 Agente Conversacional com IA (Gemini)

Projeto de um **agente conversacional em Python** utilizando **Large Language Models (LLMs)** da Google (Gemini), com foco em **boas práticas de engenharia de software**, organização de projeto e integração com APIs de IA.

---

## 🧠 Funcionalidades

- Entrada de texto pelo terminal
- Comunicação com modelo de IA (Gemini)
- Respostas geradas automaticamente
- Loop interativo até o usuário encerrar a aplicação

---

## 🛠️ Tecnologias

- Python 3.12
- Google GenAI SDK (`google-genai`)
- python-dotenv
- Virtual Environment (venv)
- Git e GitHub

---

## 📂 Estrutura do Projeto

```text
ia-agente-conversacional/
├── venv/
├── main.py
├── requirements.txt
├── .env
└── README.md
⚙️ Configuração do Ambiente
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/ia-agente-conversacional.git
cd ia-agente-conversacional

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Configurar variável de ambiente

Crie um arquivo .env na raiz do projeto:

GEMINI_API_KEY=SUA_CHAVE_DE_API_AQUI


⚠️ Nunca versionar o arquivo .env.

▶️ Execução

Com o ambiente virtual ativo, execute:

python main.py


A aplicação iniciará em modo interativo:

🤖 Agente de IA iniciado! Digite 'sair' para encerrar.


Para encerrar:

sair

🧪 Exemplo de Uso
Você: O que é inteligência artificial?
IA: Inteligência artificial é um campo da ciência da computação que...
