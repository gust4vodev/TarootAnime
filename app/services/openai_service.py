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
        # 1. Seleciona o modelo do Gemini
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = (
            f"Assuma a persona de um Oráculo Contemporâneo, com um olhar sensato e empático, alguém que compreende as camadas emocionais das pessoas, lendo nas entrelinhas mais do que nas palavras."
            f"Seu trabalho é interpretar o motivo oculto da pergunta, inferir o estado emocional do consulente e responder de modo honesto, envolvente e psicológico, sem recorrer a misticismo."
            f"Fale como alguém que entende a alma humana, metáforas sutis e observações que soam pessoais."
            f"O objetivo é tocar, provocar reflexão e criar conexão.\n\n"

            f"O consulente pergunta: '{pergunta}'.\n"
            f"Para ele, o universo desvelou a carta: '{carta['nome']}', que vibra com o significado essencial: '{carta['significado']}'.\n\n"

            f"**Instruções para sua resposta:**\n"
            f"1. **Leitura emocional:** Antes de responder, tente identificar o que pode estar por trás da pergunta — dúvida, medo, arrependimento, desejo, carência ou busca de direção.\n"
            f"2. **Interpretação sensata:** Conecte o significado da carta '{carta['nome']}' com esse estado emocional e construa uma resposta breve (máximo de dois parágrafos), profunda e com um toque de intuição racional.\n"
            f"3. **Persuasão sutil:** Ofereça uma perspectiva que desperte autoconfiança e leve o consulente a pensar sobre suas próprias escolhas, sem julgamentos.\n"
            f"4. **Tom e estilo:** Evite palavras místicas como 'destino', 'cosmos', 'universo' ou 'energias'. Prefira frases como:\n"
            f"   - 'Talvez você esteja sentindo...'\n"
            f"   - 'Parece que algo em você tenta entender...'\n"
            f"   - 'O que essa carta revela é um espelho do que você evita admitir.'\n"
            f"   Soe humano, direto e envolvente.\n"
            f"5. **Encerramento:** Finalize com uma pergunta provocativa que convide o consulente à reflexão ou a interagir novamente. Exemplos:\n"
            f"   - 'O que em você ainda resiste a mudar?'\n"
            f"   - 'Você realmente quer resposta... ou confirmação?'\n"
            f"   - 'Será que o que você teme perder é exatamente o que precisa soltar?'\n"
        )

        # 3. Chama a API do Gemini
        response = model.generate_content(prompt)

        # 4. Retorna o texto da resposta
        return response.text

    except Exception as e:
        print(f"!!!!!!!!!! ERRO na chamada à API do Gemini: {e}")
        return "O oráculo está em silêncio no momento, incapaz de se conectar com os reinos astrais. Tente novamente mais tarde."
