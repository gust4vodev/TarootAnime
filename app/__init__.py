from flask import Flask

def create_app():
    """
    Função que funciona como uma 'fábrica' para a nossa aplicação.
    Ela cria, configura e retorna a instância do app Flask.
    """
    # 1. Cria a instância do aplicativo Flask
    app = Flask(__name__)

    # 2. Encontra e registra nosso Blueprint 'main'
    # A importação é feita aqui dentro para evitar importações circulares
    from .main import main_bp
    app.register_blueprint(main_bp)

    # 3. Retorna o aplicativo montado e configurado
    return app