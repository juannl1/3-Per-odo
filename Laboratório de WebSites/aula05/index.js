function maior_menor(){
    let numero = prompt("Digite o número: ")

    if (numero > 0){
        document.getElementById('saida1').innerHTML = "Positivo"
    } else if (numero < 0){
        document.getElementById('saida1').innerHTML = "Negativo"
    } else {
        document.getElementById('saida1').innerHTML = "Zero"
    }
}

function par_impar(){
    let valor = prompt('Numero')

    if (valor % 2 == 0){
        document.getElementById('saida2').innerHTML = 'Par'
    } else {
        document.getElementById('saida2').innerHTML = 'Impar'
    }
}

function contagem_crescente(){

    let texto = ""
    for (let i=1; i < 11; i++)
        texto += i + " "
    document.getElementById('saida3').innerHTML = texto
}

function contagem_decrescente(){
    let i = 10; 
    let texto = " ";

    while (i >= 1) {
        console.log(i);
        texto += i + " ";
        i--;
    }
    document.getElementById('saida4').innerHTML = texto;
}

function gerarTabuada() {
    let num = parseInt(prompt("De qual número você deseja a tabuada?"));
    let saida = document.getElementById('saida1'); 
    
    if (isNaN(num)) {
        alert("Por favor, digite um número válido.");
        return;
    }

    let resultado = `<h3>Tabuada do ${num}</h3>`;

    for (let i = 1; i <= 10; i++) {
        let multiplicacao = num * i;
        resultado += `${num} x ${i} = ${multiplicacao}<br>`;
    }

    saida.innerHTML = resultado;
}



