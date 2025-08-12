Neste projeto, escolhi as tecnologias e a organização do código pensando em um equilíbrio entre simplicidade, aprendizado e escalabilidade futura. Como ainda estou iniciando no frontend, optei por soluções que me permitam entender bem cada etapa do processo e evoluir com segurança.

## Backend

**Linguagem e Framework:**  
Utilizo **Python** no backend, por já ter familiaridade com a linguagem e sua versatilidade.  
Para a estrutura do servidor, escolhi o **Flask** por ser um framework leve e simples, ideal para quem está começando. Ele permite criar rotas, renderizar templates HTML e oferecer APIs com facilidade, sem a complexidade de frameworks maiores. Além disso, Flask tem excelente documentação e uma comunidade ativa, o que ajuda bastante no aprendizado.

**Banco de Dados:**  
Para armazenar dados inicialmente, optei pelo **SQLite**, que é um banco de dados relacional simples, sem necessidade de configuração de servidor. É perfeito para projetos pequenos e para aprender conceitos básicos de persistência de dados. Caso o projeto cresça, posso migrar para um banco mais robusto como PostgreSQL.

**Ambiente Virtual e Dependências:**  
Uso o ambiente virtual padrão do Python, o **venv**, que isola as dependências do projeto, evitando conflitos com outras instalações. Todas as bibliotecas usadas ficam listadas no arquivo `requirements.txt`, facilitando a reprodução do ambiente em qualquer máquina.

---

## Frontend

Como estou começando a aprender frontend, decidi trabalhar com as tecnologias básicas:  
- **HTML** para estruturar o conteúdo das páginas,  
- **CSS** para estilizar e deixar o visual agradável,  
- **JavaScript puro** para criar interatividade e manipular elementos na página.

Essa escolha me ajuda a compreender de forma mais profunda o funcionamento real da web, sem depender inicialmente de frameworks complexos como React ou Vue. Mais para frente, caso eu queira, posso adicionar bibliotecas leves como Alpine.js para melhorar a interatividade sem perder a simplicidade.

---

## Integração com IA

Pretendo integrar o backend com a API da OpenAI para permitir que o app interprete as cartas e responda perguntas de forma personalizada. Essa parte é fundamental para agregar valor ao projeto, mostrando conhecimento em integração de APIs externas e inteligência artificial.

---

## Organização do Código e Estrutura de Pastas

Para manter o projeto organizado e facilitar o desenvolvimento, utilizei a seguinte estrutura de pastas:

```plaintext
tarootanime/
│
├── app/                           # Código principal da aplicação
│   ├── __init__.py                # Inicialização do Flask e configuração
│   ├── routes.py                  # Rotas e controladores web
│   ├── models.py                  # Modelos de dados e banco
│   ├── static/                    # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/                 # Templates HTML (Jinja2)
│       ├── base.html              # Layout base comum a todas páginas
│       └── index.html             # Página inicial
│
├── docs/                         # Documentação do projeto em Markdown
├── tests/                        # Testes automatizados (a implementar)
├── venv/                         # Ambiente virtual Python (não versionar)
├── requirements.txt              # Lista de dependências
├── run.py                        # Script para iniciar o servidor Flask
└── README.md                     # Documentação principal do projeto


Essa estrutura oferece uma base clara e flexível, que permite a evolução do projeto conforme meu aprendizado e a inclusão de novas funcionalidades.