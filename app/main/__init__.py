from flask import Blueprint

# Criamos o Blueprint e damos um nome a ele ('main')
# O segundo argumento, __name__, ajuda o Flask a localizar a pasta de templates
main_bp = Blueprint('main', __name__, template_folder='../templates', static_folder='../static')

# Importamos as rotas DEPOIS de criar o blueprint para evitar erros de importação
from . import routes