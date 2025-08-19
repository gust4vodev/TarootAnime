document.addEventListener('DOMContentLoaded', () => {
    // --- Selecionando os Elementos ---
    const campoPergunta = document.getElementById('campo-pergunta');
    const botaoRevelar = document.getElementById('botao-revelar');
    const fundoCartaImg = document.getElementById('fundo-carta-img');
    const videoRevelacao = document.getElementById('video-revelacao');
    const sobreposicaoResultado = document.getElementById('sobreposicao-resultado');
    const imagemCartaSorteada = document.getElementById('imagem-carta-sorteada');
    const nomeCartaSorteada = document.getElementById('nome-carta-sorteada');
    const areaResultado = document.getElementById('area-resultado');
    const tituloCartaDireita = document.getElementById('titulo-carta-direita');
    const textoSignificadoCarta = document.getElementById('texto-significado-carta');
    const areaRespostaOraculo = document.getElementById('area-resposta-oraculo');
    const textoRespostaOraculo = document.getElementById('texto-resposta-oraculo');

    // --- FUNÇÃO FICTÍCIA (NOSSO PLANO B / FALLBACK) ---
    // Chamada quando o usuário está offline ou o servidor falha.
    async function simularChamadaBackend(pergunta) {
        console.log("MODO FALLBACK ATIVADO: Usando resposta fictícia.");
        await new Promise(resolve => setTimeout(resolve, 1500)); // Simula atraso
        
        const respostaJSON = { 
            "id": 1, 
            "nome": "O Louco", 
            "significado": "Novos começos, espontaneidade, aventura, fé",
            "resposta": "" // Começa com a resposta vazia
        };

        if (pergunta.trim() !== '') {
            respostaJSON.resposta = `(Fallback) Com base em O Louco, sua pergunta sobre "${pergunta.substring(0,20)}..." revela um espírito aventureiro.`;
        }
        return respostaJSON;
    }

    // --- FUNÇÃO REAL QUE CHAMA O BACKEND (PLANO A) ---
    async function buscarRespostaDoBackend(pergunta) {
        try {
            // Tenta a chamada real
            const response = await fetch('/api/obter_resposta', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pergunta: pergunta }),
            });
            if (!response.ok) {
                // Se o servidor responder com um erro (ex: 404, 500), joga um erro.
                throw new Error('Servidor respondeu com erro.');
            }
            console.log("Conexão com backend bem-sucedida!");
            return await response.json();
        } catch (error) {
            // Se a chamada real falhar por qualquer motivo (sem internet, servidor offline)...
            console.warn("AVISO: Falha ao contatar o backend. Ativando modo fallback.", error);
            // ...chama a função fictícia como plano B!
            return await simularChamadaBackend(pergunta);
        }
    }

    // --- Evento de Clique (Não muda) ---
    botaoRevelar.addEventListener('click', async () => {
        const perguntaDoUsuario = campoPergunta.value;

        // Prepara a interface...
        botaoRevelar.disabled = true;
        sobreposicaoResultado.style.opacity = '0';
        areaResultado.style.opacity = '0';
        areaRespostaOraculo.style.display = 'none';

        // Inicia a animação...
        fundoCartaImg.style.opacity = '0';
        videoRevelacao.style.opacity = '1';
        videoRevelacao.currentTime = 0;
        videoRevelacao.play();

        // Chama o backend (que agora tem o fallback embutido)
        const dadosDaCarta = await buscarRespostaDoBackend(perguntaDoUsuario);

        // Quando a animação do vídeo terminar...
        videoRevelacao.onended = () => {
            videoRevelacao.style.opacity = '0';

            // Preenche os slots com os dados (reais ou fictícios)
            imagemCartaSorteada.src = `/static/img/${dadosDaCarta.id}.jpg`;
            nomeCartaSorteada.textContent = dadosDaCarta.nome;
            tituloCartaDireita.textContent = dadosDaCarta.nome;
            textoSignificadoCarta.textContent = dadosDaCarta.significado;
            textoRespostaOraculo.textContent = dadosDaCarta.resposta;

            // Exibe os resultados
            sobreposicaoResultado.style.opacity = '1';
            areaResultado.style.opacity = '1';
            
            if (dadosDaCarta.resposta) {
                areaRespostaOraculo.style.display = 'block';
            }

            // Reseta para o próximo sorteio
            fundoCartaImg.style.opacity = '1';
            botaoRevelar.disabled = false;
        };
    });
});