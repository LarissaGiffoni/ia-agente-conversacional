# 🤖 Agente de IA Conversacional com Gemini

## ✨ Visão Geral do Projeto

Este projeto implementa um agente de inteligência artificial simples, utilizando a API do Google Gemini. O agente é capaz de receber entradas de texto do usuário via console (terminal) e retorna respostas geradas pelo modelo de linguagem, mantendo o contexto de conversas anteriores (memória).

O objetivo principal é demonstrar a integração fundamental entre Python e o SDK do Gemini para criar aplicações conversacionais.

---

## 🚀 Tecnologias e Recursos

* **Linguagem:** Python
* **SDK:** Google GenAI SDK
* **Modelo de IA:** `gemini-2.5-flash` (Otimizado para tarefas rápidas e conversacionais)
* **Segurança:** `python-dotenv` para gerenciamento seguro da chave de API (`.env`).
* **Funcionalidade Principal:** Implementação de Histórico de Conversa (Memória).

---

## ⚙️ Configuração e Execução Local

Siga os passos abaixo para rodar o agente no seu ambiente.

### 1. Pré-requisitos

Certifique-se de ter:
* Python 3.x instalado.
* Uma chave de API do Google Gemini, obtida no Google AI Studio.

### 2. Clonar o Repositório

```bash
git clone [https://github.com/LarissaGiffoni/ia-agente-conversacional.git](https://github.com/LarissaGiffoni/ia-agente-conversacional.git)
cd ia-agente-conversacional

### 3. Instalar Dependências

Crie e ative seu ambiente virtual (`venv`) e instale as dependências listadas no `requirements.txt`:

```bash
# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Instala as dependências
pip install -r requirements.txt
