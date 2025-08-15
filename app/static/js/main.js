document.addEventListener('DOMContentLoaded', () => {
    // --- O array 'cards' não é mais necessário, os dados vêm da simulação ---

    // --- Selecionando os Elementos ---
    const campoPergunta = document.getElementById('campo-pergunta');
    const botaoRevelar = document.getElementById('botao-revelar');
    const fundoCartaImg = document.getElementById('fundo-carta-img');
    const videoRevelacao = document.getElementById('video-revelacao');
    const sobreposicaoResultado = document.getElementById('sobreposicao-resultado');
    const imagemCartaSorteada = document.getElementById('imagem-carta-sorteada');
    const nomeCartaSorteada = document.getElementById('nome-carta-sorteada');
    const areaResultado = document.getElementById('area-resultado');
    const textoSignificadoCarta = document.getElementById('texto-significado-carta');
    const areaRespostaOraculo = document.getElementById('area-resposta-oraculo');
    const textoRespostaOraculo = document.getElementById('texto-resposta-oraculo');
    const tituloCartaDireita = document.getElementById('titulo-carta-direita');

    // --- FUNÇÃO QUE SIMULA A CHAMADA AO BACKEND ---
    async function simularChamadaBackend(pergunta) {
        // ...
        return { 
            "id": 1, 
            "nome": "O Louco", // <-- O nome é definido aqui
            "significado": "Novos começos, espontaneidade, aventura, fé",
            "resposta": "Sua cor favorita provavelmente é amarelo, refletindo alegria, espontaneidade e novas experiências isso se conecta com O Louco, que simboliza aventura e abertura para o novo."
        };
    }

    // --- Evento de Clique ---
    botaoRevelar.addEventListener('click', async () => {
        // Captura a pergunta do usuário AQUI
        const perguntaDoUsuario = campoPergunta.value;

        // 1. Resetar e preparar a interface
        botaoRevelar.disabled = true;
        sobreposicaoResultado.style.opacity = '0';
        areaResultado.style.opacity = '0';
        areaRespostaOraculo.style.display = 'none'; // Sempre esconde a resposta antiga

        // 2. Iniciar a animação visual
        fundoCartaImg.style.opacity = '0';
        videoRevelacao.style.opacity = '1';
        videoRevelacao.currentTime = 0;
        videoRevelacao.play();

        // 3. NOS BASTIDORES: Chamar o backend SIMULADO
        const dadosDaCarta = await simularChamadaBackend(perguntaDoUsuario);

        // 4. Quando a animação do vídeo terminar...
        videoRevelacao.onended = () => {
            // 5. Esconder o vídeo
            videoRevelacao.style.opacity = '0';

            // 6. Preencher os slots com os dados recebidos
            imagemCartaSorteada.src = `/static/img/${dadosDaCarta.id}.jpg`;
            nomeCartaSorteada.textContent = dadosDaCarta.nome;
            tituloCartaDireita.textContent = dadosDaCarta.nome;
            textoSignificadoCarta.textContent = dadosDaCarta.significado;
            textoRespostaOraculo.textContent = dadosDaCarta.resposta;

            // 7. Exibir a carta e o significado
            sobreposicaoResultado.style.opacity = '1';
            areaResultado.style.opacity = '1';
            
            // 8. LÓGICA CONDICIONAL PARA A RESPOSTA DO ORÁCULO
            if (dadosDaCarta.resposta) { // (string vazia é 'false')
                areaRespostaOraculo.style.display = 'block';
            }

            // 9. Resetar para o próximo sorteio
            fundoCartaImg.style.opacity = '1';
            botaoRevelar.disabled = false;
        };
    });
});