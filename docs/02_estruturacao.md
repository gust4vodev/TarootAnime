# Arquitetura e Organização do Projeto

Neste projeto, busquei equilibrar simplicidade, aprendizado e espaço para crescer no futuro.  
Como ainda estou construindo minha base no desenvolvimento frontend, escolhi ferramentas e padrões que me permitissem entender cada etapa a fundo, evoluindo com segurança.

---

## Backend

**Linguagem e Framework**  
Optei por **Python** no backend, pela familiaridade e versatilidade da linguagem.  
Para o servidor, escolhi o **Flask** — leve, direto e perfeito para quem quer aprender os fundamentos sem a complexidade de frameworks maiores. Ele permite criar rotas, renderizar templates e expor APIs de forma simples, com documentação clara e uma comunidade ativa que facilita a resolução de dúvidas.

**Banco de Dados**  
Comecei com **SQLite**, banco relacional simples que dispensa configuração de servidor. É ideal para projetos pequenos e para aprender os conceitos básicos de persistência. Se o projeto crescer, a migração para algo mais robusto, como PostgreSQL, será tranquila.

**Ambiente Virtual e Dependências**  
Uso o **venv** para isolar dependências, evitando conflitos com outros projetos.  
Todas as bibliotecas ficam listadas em `requirements.txt`, facilitando a reprodução do ambiente em qualquer máquina.

---

## Frontend

Para construir o frontend, optei por ir no essencial:  
- **HTML** para estruturar o conteúdo,  
- **CSS** para definir o visual,  
- **JavaScript puro** para criar interatividade.

Essa escolha me permite compreender como a web funciona na base, antes de partir para frameworks como React ou Vue.  
Mais adiante, posso incluir bibliotecas leves, como Alpine.js, para aumentar a interatividade sem perder a simplicidade.

---

## Integração com IA

O backend será integrado à API da OpenAI para interpretar as cartas e responder perguntas de forma personalizada.  
Essa funcionalidade trará valor ao projeto e mostrará domínio em integrações com APIs externas e inteligência artificial.

---

## Estrutura de Pastas

Organizei o projeto de forma modular e clara:

```plaintext
tarootanime/
│
├── app/                           # Código principal
│   ├── __init__.py                # Configuração do Flask
│   ├── routes.py                  # Rotas e controladores
│   ├── models.py                  # Modelos e banco
│   ├── static/                    # CSS, JS e imagens
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/                 # Templates HTML (Jinja2)
│       ├── base.html               # Layout base
│       └── index.html              # Página inicial
│
├── docs/                          # Documentação em Markdown
├── tests/                         # Testes automatizados (futuros)
├── venv/                          # Ambiente virtual (ignorado no Git)
├── requirements.txt               # Dependências
├── run.py                         # Inicialização do servidor
└── README.md                      # Documentação principal
