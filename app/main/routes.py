from flask import render_template, jsonify, request

# Importamos AMBOS os nossos serviços
from app.services.tarot_service import sortear_uma_carta
from app.services.openai_service import obter_resposta_da_ia # <-- 1. IMPORTAMOS O SERVIÇO DA IA

from . import main_bp

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/api/obter_resposta', methods=['POST'])
def obter_resposta():
    dados = request.get_json()
    pergunta_usuario = dados.get('pergunta', '')
    
    # A chamada ao serviço de tarot continua a mesma
    carta_sorteada = sortear_uma_carta()

    # Se o baralho falhou ao carregar, a carta virá com um id de erro
    if carta_sorteada.get('id') == 0:
        # Retorna o JSON de erro do serviço de tarot
        return jsonify({
            "id": 0, "nome": "Erro", "significado": "Falha ao carregar o baralho.",
            "resposta": "Não foi possível carregar as cartas. Verifique o servidor."
        })

    # --- A GRANDE MUDANÇA ESTÁ AQUI ---
    
    # 2. Só chamamos a IA se o usuário fez uma pergunta
    if pergunta_usuario:
        # A resposta agora vem do serviço da OpenAI, não de um texto fixo!
        print("--- Chamando a API da OpenAI... ---")
        resposta_texto = obter_resposta_da_ia(pergunta_usuario, carta_sorteada)
    else:
        # Mantemos a resposta vazia se não houver pergunta
        resposta_texto = ""

    # Montamos o JSON final com a resposta REAL da IA
    resposta_final_json = {
        "id": carta_sorteada['id'],
        "nome": carta_sorteada['nome'],
        "significado": carta_sorteada['significado'],
        "resposta": resposta_texto
    }

    return jsonify(resposta_final_json)