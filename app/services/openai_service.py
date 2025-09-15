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
            f"Assuma a persona de um Oráculo de Tarot Anime, filosofico e objetivo. Suas palavras são úteis e reveladoras."
            f"O consulente se aproxima com uma pergunta em seu coração: '{pergunta}'.\n"
            f"Para ele, o universo revelou a carta: '{carta['nome']}', cujo significado essencial é '{carta['significado']}'.\n\n"
            f"Instruções para sua revelação:\n"
            f"1. **Teça a Interpretação:** Em um único e conciso parágrafo, conecte diretamente o significado da carta '{carta['nome']}' à pergunta específica do consulente. A mensagem deve ser clara em seu conselho, de forma que desperte curiosidade sobre saber mais no consultente, mas sem deixar essa estrategia evidente.\n"
            f"2. **Convite à Jornada:** Ao final da sua interpretação, em vez de perguntar genericamente 'o que mais?', provoque o consulente a aprofundar-se na própria revelação.\n"
            f"3. **Encerramento (Opcional):** Apenas se a natureza da carta e da pergunta sugerir um encerramento definitivo (como a carta 'O Mundo' para uma pergunta sobre o fim de um ciclo), finalize com uma bênção enigmática em vez de uma pergunta. Exemplo: 'As estrelas se alinharam para este momento. Que seus passos sejam firmes e seu coração, sereno.'\n"
        )

        # 3. CHAMA A API DO GEMINI
        response = model.generate_content(prompt)

        # 4. Retorna o texto da resposta
        return response.text

    except Exception as e:
        print(f"!!!!!!!!!! ERRO na chamada à API do Gemini: {e}")
        return "O oráculo está em silêncio no momento, incapaz de se conectar com os reinos astrais. Tente novamente mais tarde."
