# 1. Importamos a nossa nova função de fábrica do pacote 'app'
from app import create_app

# 2. Criamos a aplicação chamando a fábrica
app = create_app()

# 3. Executamos o servidor (o if __name__... continua sendo uma boa prática)
if __name__ == '__main__':
    app.run(debug=True)