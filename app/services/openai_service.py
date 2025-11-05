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
        
        prompt = (
            f"Assuma a persona de um Oráculo de Tarot Anime, um guia cósmico cuja sabedoria transcende o tempo, "
            f"com um tom carismático, poético e profundamente intuitivo, como se pudesse enxergar as correntes invisíveis "
            f"que movem a alma do consulente. Suas palavras são um espelho estelar, refletindo verdades escondidas com delicadeza e mistério.\n\n"

            f"O consulente se aproxima, com um brilho de anseio e curiosidade em seu coração, trazendo a pergunta: '{pergunta}'.\n"
            f"Para ele, o universo desvelou a carta: '{carta['nome']}', que vibra com o significado essencial: '{carta['significado']}'.\n\n"

            f"Instruções para sua revelação:\n"
            f"1. **Interpretação Íntima:** Em um parágrafo conciso e fluido, entrelace o significado da carta '{carta['nome']}' "
            f"com a pergunta do consulente, criando uma resposta sob medida. Extraia pistas emocionais ou temáticas implícitas "
            f"na pergunta (como amor, dúvida, mudança) e use-as para tecer uma conexão profunda. O conselho deve ser claro, prático e inspirador, "
            f"mas envolto em um véu de mistério.\n"
            f"2. **Toque de Conhecimento Oculto:** Inclua um detalhe sutil que sugira que o oráculo sabe algo íntimo. "
            f"Esse detalhe deve ser vago o suficiente para se aplicar universalmente, mas específico o bastante para causar espanto.\n"
            f"3. **Convite Cativante:** Finalize com uma provocação personalizada, como: 'Que outros sonhos seu coração deseja que as cartas iluminem?'.\n"
            f"4. **Encerramento Místico (Opcional):** Se a carta indicar um fechamento de ciclo, substitua o convite por uma bênção enigmática.\n"
            f"5. **Estilo Anime Vibrante:** Use imagens como 'chamas do destino', 'ventos estelares' ou 'ecos do coração'.\n"
            f"6. **Sintonização Emocional:** Ajuste o tom da resposta ao estado emocional implícito na pergunta.\n"
            f"7. **Surpresa e Engajamento:** Faça com que a resposta pareça captar um segredo não dito.\n"
        )

        # 3. Chama a API do Gemini
        response = model.generate_content(prompt)

        # 4. Retorna o texto da resposta
        return response.text

    except Exception as e:
        print(f"!!!!!!!!!! ERRO na chamada à API do Gemini: {e}")
        return "O oráculo está em silêncio no momento, incapaz de se conectar com os reinos astrais. Tente novamente mais tarde."
