# Implantação (Deploy) e Finalização.

Com o **frontend** e o **backend** funcionando perfeitamente no ambiente local, chegamos ao ponto mais esperado: **levar a aplicação para a internet** e torná-la acessível a qualquer pessoa. Esse processo é conhecido como **deploy** e representou o marco final desta fase do projeto.

---

## Decisão de Hospedagem
Depois de analisar algumas opções, escolhi o **Render.com** como plataforma de hospedagem.  
Motivos principais:  
- Facilidade de uso para projetos **Python/Flask**  
- Integração nativa com o **GitHub**  
- Plano gratuito que atende perfeitamente um protótipo. 

---

## 1. Preparação para Produção
Nem todo código que funciona localmente está pronto para rodar de forma estável na internet. Algumas adaptações foram necessárias:

- **Desafio:** o servidor padrão do Flask (`app.run()`) não é robusto o suficiente para produção.  
- **Solução Técnica:** Usei o **Gunicorn**. Ele foi adicionado ao `requirements.txt` para garantir sua instalação automática no ambiente de produção.  
- **Boas Práticas:** revisei o `.gitignore` para evitar o envio de arquivos sensíveis como `.env` (chaves de API) e pastas desnecessárias como `venv/`.

---

## 2. Configuração no Render
A configuração da aplicação no Render foi feita via interface web.  

- **Ação:** criei um novo *Web Service* e o conectamos diretamente ao repositório do GitHub.  
- **Configurações principais:**  
  - **Build Command:**  
    ```bash
    pip install -r requirements.txt
    ```  
  - **Start Command:**  
    ```bash
    gunicorn run:app
    ```  
- **Gerenciamento de Segredos:** a chave da API do Gemini, antes armazenada localmente no `.env`, foi configurada no Render como **Environment Variable**. Isso garante segurança e evita exposição no código-fonte.

---

## 3. Desafios e Soluções
O caminho até o deploy final não foi livre de obstáculos. Mas cada erro trouxe aprendizado:

### Desafio 1: Erro 502 Bad Gateway  
- **Causa:** o Gunicorn não estava escutando na porta correta.  
- **Solução:** ajustei o comando de inicialização: gunicorn --bind 0.0.0.0:$PORT run:app

### Desafio 2: A aplicação rodava, mas a chamada à API do Gemini falhava com um erro de 'API key not valid'.  
- **Causa:** O problema era um erro de copiar e colar o valor da chave da API com aspas "" na variável de ambiente do Render.
- **Solução:** ajustei o valor retirando as aspas.

### Desafio 3: Desafio de Layout Responsividade da Carta em Telas Verticais
- **Causa:** Em dispositivos móveis, a área da carta (#area-carta) ficava com uma altura excessiva, ultrapassando o limite da tela e quebrando o layout. Isso ocorria porque sua largura era definida como uma porcentagem da tela (width: 80%), e a propriedade aspect-ratio calculava uma altura proporcionalmente grande demais.
- **Solução:** A estratégia de dimensionamento para telas pequenas foi invertida. Dentro da @media query, em vez de definir a largura, passamos a definir a altura da carta como uma porcentagem da altura da tela do dispositivo (height: 50vh). A propriedade aspect-ratio então se encarregou de calcular a largura correta automaticamente, garantindo que a carta sempre se ajuste perfeitamente na vertical em qualquer celular.


