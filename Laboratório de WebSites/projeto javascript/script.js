document.addEventListener("DOMContentLoaded", () => {
    const videoElemento = document.getElementById("meuVideo");
    const btnPlay = document.getElementById("btnPlay");
    const btnPause = document.getElementById("btnPause");
    const btnMudarVideo = document.getElementById("btnMudarVideo");

    btnPlay.addEventListener("click", () => {
        videoElemento.play();
    });

    btnPause.addEventListener("click", () => {
        videoElemento.pause();
    });

    // Manipulação do DOM
    btnMudarVideo.addEventListener("click", () => {
        videoElemento.src = "https://www.w3schools.com/html/movie.mp4";
        videoElemento.load(); 
        videoElemento.play(); 
    });

    const formulario = document.getElementById("meuFormulario");
    const idadeInput = document.getElementById("idade");
    const cupomInput = document.getElementById("cupom");
    const feedbackDiv = document.getElementById("mensagemFeedback");

    formulario.addEventListener("submit", (event) => {
        // Impede a página de recarregar
        event.preventDefault();

        const idade = Number(idadeInput.value);
        const cupom = cupomInput.value;

        // Limpa mensagens anteriores
        feedbackDiv.className = "mensagem-oculta";

        if (idade < 18) {
            feedbackDiv.textContent = "Erro: Você precisa ser maior de 18 anos para prosseguir.";
            feedbackDiv.className = "mensagem-oculta erro";
            return;
        }

        if (cupom !== "SOUALUNO") {
            feedbackDiv.textContent = "Erro: Cupom inválido! Dica: use o cupom SOUALUNO.";
            feedbackDiv.className = "mensagem-oculta erro";
            return; 
        }

        feedbackDiv.textContent = "Sucesso! Idade permitida e cupom aplicado.";
        feedbackDiv.className = "mensagem-oculta sucesso";
        
        formulario.reset();
    });
});