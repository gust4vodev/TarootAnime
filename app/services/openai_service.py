import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do seu arquivo .env
load_dotenv()

# Configura a chave de API do Google Gemini a partir da variável de ambiente
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"!!!!!!!!!! ERRO no gemini_service: Falha ao configurar a API do Gemini. Verifique a chave no .env. Erro: {e}")

def obter_resposta_da_ia(pergunta, carta):
    """
    Envia a pergunta e os dados da carta para a IA do Gemini
    e retorna a resposta em texto gerada por ela.
    """
    try:
        # 1. Seleciona o modelo do Gemini que queremos usar
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        # 2. Nosso prompt de alta qualidade continua o mesmo!
        prompt = (
            f"Aja como um oráculo de tarot místico, sábio e poético. "
            f"Um consulente fez a seguinte pergunta: '{pergunta}'.\n"
            f"A carta sorteada para ele foi '{carta['nome']}', que tem o significado principal de '{carta['significado']}'.\n\n"
            f"Com base na carta sorteada e em seu significado, formule uma resposta provocativa e reflexiva para a pergunta do consulente. "
            f"A resposta deve curta em um único parágrafo e ter um tom enigmático, mas útil."
        )

        # 3. CHAMA A API DO GEMINI
        response = model.generate_content(prompt)

        # 4. Retorna o texto da resposta
        return response.text

    except Exception as e:
        print(f"!!!!!!!!!! ERRO na chamada à API do Gemini: {e}")
        return "O oráculo está em silêncio no momento, incapaz de se conectar com os reinos astrais. Tente novamente mais tarde."