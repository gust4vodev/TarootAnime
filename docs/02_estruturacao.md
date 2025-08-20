# Arquitetura e Organização do Projeto

Neste projeto, busquei equilibrar simplicidade, aprendizado e espaço para crescer no futuro.  
Como ainda estou construindo minha base no desenvolvimento frontend, escolhi ferramentas e padrões que me permitissem entender cada etapa a fundo, evoluindo com segurança.

---

## Backend

**Linguagem e Framework**  
Optei por **Python** no backend, pela familiaridade e versatilidade da linguagem.  
Para o servidor, escolhi o **Flask** — leve, menor curva de aprendizado, para praticar sem a complexidade de frameworks maiores. Ele permite criar rotas, renderizar templates e expor APIs de forma simples.
**Banco de Dados**  
Desde o início do projeto, percebi que não seria necessário utilizar um banco de dados, pois não teríamos dados de usuários para armazenar, apenas o essencial para o funcionamento do TarootAnime.  
Futuramente, caso decidir implementar funcionalidades como sessões personalizadas ou controle de usuários, poderemos avaliar a adição de um banco, como **SQLite** ou **PostgreSQL**, conforme a necessidade.

**Ambiente Virtual e Dependências**  
Usar o **venv** para isolar dependências, evitando conflitos com outros projetos.  
Todas as bibliotecas serão listadas em `requirements.txt`, facilitando a reprodução do ambiente em qualquer máquina.

---

## Frontend

Para construir o frontend, optei por ir no essencial:  
- **HTML** para estruturar o conteúdo,  
- **CSS** para definir o visual,  
- **JavaScript puro** para criar interatividade.

Essa escolha me permite evoluir na compreenção de como a web funciona na base, antes de partir para frameworks como React ou Vue.  
Mais adiante, posso incluir outras bibliotecas, para aumentar a interatividade sem perder a simplicidade.

---

## Integração com IA

O backend será integrado à API do Gemini para interpretar as cartas e responder perguntas de forma personalizada.  
Essa funcionalidade trará valor ao projeto e mostrará domínio em integrações com APIs externas e inteligência artificial.

---

## Organização do Código

Desde o início, minha ideia é manter o código o mais modular possível.  
Isso me ajudará a **enxergar o projeto de forma clara**, do começo ao fim, e facilita bastante na hora de debugar ou fazer alterações.

A ideia é que, conforme o projeto evoluir, cada componente, rotas, templates, arquivos estáticos, lógica do backend, esteja organizado de forma separada e bem definida, tornando o desenvolvimento mais simples, limpo e escalável.