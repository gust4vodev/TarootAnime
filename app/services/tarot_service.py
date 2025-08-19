import json
import os
import random

def _carregar_baralho():
    """
    Função interna para encontrar e carregar o baralho do arquivo JSON.
    Retorna uma lista de cartas ou um dicionário de erro.
    """
    try:
        # O caminho agora é relativo a ESTE arquivo (que está dentro de app/services)
        base_dir = os.path.abspath(os.path.dirname(__file__))
        # Subimos 1 nível para a pasta 'app', depois descemos para a pasta 'data'
        json_path = os.path.join(base_dir, '..', 'data', 'tarrotanime.json')
        
        with open(json_path, 'r', encoding='utf-8') as f:
            baralho_completo = json.load(f)
        print(f"--- Módulo Tarot: Baralho com {len(baralho_completo)} cartas carregado! ---")
        return baralho_completo
    except Exception as e:
        print(f"!!!!!!!!!! ERRO no tarot_service: Não foi possível carregar o baralho. Erro: {e}")
        return [{"id": 0, "nome": "Erro de Baralho", "significado": "Falha ao carregar as cartas."}]

# A variável BARALHO é carregada uma única vez quando a aplicação inicia
BARALHO = _carregar_baralho()

def sortear_uma_carta():
    """
    Sorteia uma carta aleatória do baralho carregado.
    Retorna um dicionário representando a carta sorteada.
    """
    if not BARALHO or BARALHO[0]['id'] == 0:
        return BARALHO[0] # Retorna a carta de erro se o baralho estiver vazio ou com erro
    return random.choice(BARALHO)