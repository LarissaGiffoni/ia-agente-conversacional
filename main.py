import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# 1. Cria o client usando a chave de API do arquivo .env
# Certifique-se de que a variável de ambiente se chama "GEMINI_API_KEY" no seu arquivo .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. REMOVA OU COMENTE ESTA LINHA:
# # Altere a linha do modelo para usar a versão v1
# client.set_api_version('v1') # <-- Esta linha está causando o erro!

print("🤖 Agente de IA iniciado! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")

    if user_input.lower() == "sair":
        print("👋 Encerrando agente.")
        break

    # 3. Chamada para a API
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        print("\nIA:", response.text, "\n")
    except Exception as e:
        # Adicione um bloco try/except para capturar possíveis erros da API
        print(f"\n🚫 Erro ao gerar conteúdo: {e}\n")