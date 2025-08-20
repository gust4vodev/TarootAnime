# Desenvolvimento do Backend: da Estrutura Modular à Integração com IA

## 1. Arquitetura Modular e Refatoração

Desde o início, a ideia era manter o código o mais modular possível, mesmo que no começo isso não estivesse totalmente implementado.  

- **Desafio:** Organizar o código de forma clara, preparando-o para crescer, especialmente com a futura integração da IA.  
- **Decisão:** Adotar uma arquitetura modular, seguindo boas práticas do Flask. 
- **Solução Técnica:**  
  - **Application Factory:** Mover a criação do app Flask para uma função `create_app()` em `app/__init__.py`. Foi algo novo para mim, mas tornou os testes mais fáceis e deu mais controle sobre a aplicação.  
  - **Blueprints:** Organizar as rotas em um `Blueprint` chamado `main`, deixando o código mais lógico e pronto para expansão.  
  - **Camada de Serviços:** Criar `app/services/` para separar a lógica de negócio da lógica web, ajudando a entender melhor a separação de responsabilidades. 

---

## 2. Gerenciamento de Dados: O Baralho de Tarot

Manter as 78 cartas organizadas de forma idependente do código.  

- **Desafio:** Encontrar uma forma de gerenciar os dados das cartas de maneira mais profissional e flexível.  
- **Decisão:** Mover os dados para um arquivo externo `tarrotanime.json`, separando-os do código.  
- **Solução Técnica:**  
  - Criei `app/services/tarot_service.py` só para gerenciar as cartas, o que deixou o código mais limpo.  
  - Configurei o carregamento do JSON na inicialização do app, o que melhorou a performance.  
  - **Desafio enfrentado:** Tive um problema com `FileNotFoundError` por causa de caminhos relativos. Resolvi usando `os.path.join` para ajustar o acesso ao arquivo em `app/data/`.  

---

## 3. Integração com a Inteligência Artificial (Gemini)

Integrar a IA foi uma das partes que mais gostei no projeto, especialmente porque já tenho experiência com consumo e integração de APIs.  
Meu objetivo era que o Oráculo respondesse de forma personalizada, mantendo o clima místico do projeto.

- **Desafio:** Garantir que a conexão entre backend e API do Gemini fosse segura, eficiente e confiável.  
- **Decisões e Soluções:**  
  - **Módulo Dedicado:** Criei `app/services/gemini_service.py` para isolar a lógica da IA, mantendo o código organizado e modular.  
  - **Segurança da API Key:** Usei `.env` com `python-dotenv` para proteger a chave e adicionei `.env` ao `.gitignore`.  
  - **Engenharia de Prompt:** Ajustei o prompt para que a IA respondesse como um “oráculo místico e poético”, incluindo o nome e significado da carta sorteada para manter a temática.  
  - **Tratamento de Erros:** Adicionei blocos `try...except` para lidar com falhas na API, como problemas de conexão, retornando mensagens amigáveis ao usuário.  
  - **Aprendizado técnico:** Enfrentei um erro 404 quando o modelo `gemini-pro` não estava mais disponível, mas atualizando para `gemini-1.5-flash-latest` consegui resolver rapidamente.
 

---

## 4. A API Final: Ponto de Conexão com o Frontend

Depois de estruturar os serviços, simplifiquei `app/main/routes.py` para atuar como um “orquestrador” do fluxo:  

1. Recebe a requisição do frontend.  
2. Chama `tarot_service` para sortear uma carta.  
3. Chama `gemini_service` para gerar a resposta do Oráculo.  
4. Monta o JSON final e envia para o frontend.  

---

**Resultado Final:**  
Consegui construir um backend modular, seguro e escalável, que está pronto para se conectar com o frontend.  
Durante esse processo, aprendi bastante sobre organização de código, integração com APIs e tratamento de erros, consolidando conhecimentos que já tinha e explorando novas soluções.  
Sinto que agora a base está sólida, mas ainda vejo espaço para muitas melhorias à medida que o projeto evoluir.