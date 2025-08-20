# Design, Protótipo e Desenvolvimento da Interface

## 1. Criação das Artes das Cartas

Decidi começar pela criação das imagens das cartas.  
Utilizei o ChatGPT para gerar uma lista completa com o nome e o significado das 78 cartas, organizando tudo em uma planilha.  

A partir dessa base, solicitei ao ChatGPT que, para cada carta listada, elaborasse um prompt detalhado para geração de imagens no estilo anime, destacando as características únicas de cada uma.  

Com os prompts prontos, usei o gerador de imagens gratuito do Bing para criar as artes das 78 cartas, garantindo uma identidade visual original, coerente e totalmente alinhada ao tema anime do projeto.

---

## 2. Protótipo da Interface

Após definir a identidade visual das cartas, iniciei o desenvolvimento da interface, combinada ao *vibe coding* assistido por IA, utilizando o Gemini Pro, da Google.  

Optei por trabalhar com tecnologias que ja tenho familiaridade: Flask, HTML, CSS e JavaScript puro — para focar no aprendizado dos conceitos essenciais da web. O desenvolvimento seguiu um fluxo de “passos curtos”: cada pequena funcionalidade era construída, testada e validada antes de prosseguir, garantindo um progresso sólido.  

Comecei pela estrutura HTML e um servidor Flask para “servir” a página. Em seguida, apliquei o CSS para moldar o visual, buscando transmitir o clima místico definido na identidade visual.

---

## 3. Registro de Desenvolvimento: A Interface

### Etapa 1: Fundações e Estrutura do Layout

O primeiro passo foi estabelecer a base da aplicação.

- **Decisão:** Layout de duas colunas, aproveitando melhor o espaço em telas maiores e separando a área visual (carta) da área de interação (texto e botões).  
- **Solução Técnica:** CSS Flexbox no container principal para criar as colunas (`#coluna-esquerda` e `#coluna-direita`).  

---

### Etapa 2: O Sorteio da Carta — Interatividade e Animação

- **Desafio:** Criar uma transição suave e “mágica” para o momento do sorteio.  
- **Soluções e Evolução:**  
  - **Animação:** Parti de uma exibição simples apenas exibindo a arte da carta para o usuário. Até evoluir para um esquema em camadas: carta “de costas” → vídeo de cartas girando → carta sorteada ao final do vídeo.  
  - **Transições Suaves:** Sistema de *cross-fade* controlado por JavaScript (manipulando `opacity`) e suavizado pelo CSS (`transition`).  
  - **Consistência Visual:** Aplicação das mesmas propriedades `transform` (`scale`, `rotateX`, `rotateY`) à imagem inicial, ao vídeo e à moldura, criando transições fluídas.

---

### Etapa 3: Exibição do Resultado — O Efeito de “Slot Dinâmico”

Esta foi a parte mais complexa do processo.

- **Desafio:** Garantir que a carta sorteada aparecesse perfeitamente encaixada em um formato padrão, mantendo a unidade visual do baralho (as imagens geradas são “puras” e não possuem a moldura padrão que as faz parecer cartas de um mesmo baralho).  
- **Soluções:**  
  - Primeira tentativa com `clip-path` no CSS para recortar e encaixar a carta sorteada — resultado insatisfatório.  
  - Solução final: criação de uma moldura com centro transparente (usando Photopea). No resultado, a carta sorteada é exibida abaixo da moldura, criando efeito de profundidade e acabamento visual refinado.

---

### Etapa 4: Polimento Fino e Responsividade

- **Design Responsivo:**  
  - CSS com unidades relativas (`rem`, `%`) e uso de `aspect-ratio` para manter proporções.  
  - *Media query* adaptando o layout de duas colunas para uma coluna única em telas menores.

---

### Etapa 5: Finalização do Frontend

- **Botão Único:** Unificação dos botões “Revelar Carta” e “Pedir Resposta” em “Consultar o Oráculo”, simplificando o fluxo.  
- **Fallback do Backend:** Função `async` em JavaScript simulando a chamada à API, retornando JSON no formato que tenho em mente para o backend real.  
- **Lógica Condicional:** A “Resposta do Oráculo” só aparece se o usuário tiver digitado uma pergunta; caso contrário, apenas a carta e seu significado são exibidos.

---

**Resultado Final:**  
Frontend 100% funcional, visualmente polido, responsivo e com experiência de usuário bem definida, pronto para integração com o backend.
