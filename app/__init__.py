print("--- 2. Entramos em app/__init__.py ---")
from flask import Flask

app = Flask(__name__)
print("--- 3. App Flask criado. Agora, buscando as rotas... ---")

from .routes import routes  