import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Cria o client com a chave de API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. 🔄 Inicializa o Histórico de Conversa (Novo)
# Comece com uma instrução de sistema para dar contexto à IA
history = [
    {"role": "user", "parts": ["Você é um agente de IA útil e amigável. Responda de forma concisa e em português."]},
    {"role": "model", "parts": ["Entendido. Como posso ajudar você hoje?"]}
]

print("🤖 Agente de IA iniciado! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")

    if user_input.lower() == "sair":
        print("👋 Encerrando agente.")
        break

    try:
        # 2. ➕ Adiciona a mensagem do usuário ao histórico ANTES da chamada
        history.append({"role": "user", "parts": [user_input]})

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            # 3. 🧠 Passa o histórico completo para a IA
            contents=history 
        )
        
        # 4. ➕ Adiciona a resposta da IA ao histórico DEPOIS da chamada
        history.append({"role": "model", "parts": [response.text]})

        print("\nIA:", response.text, "\n")
        
    except Exception as e:
        print(f"\n🚫 Erro ao gerar conteúdo: {e}\n")