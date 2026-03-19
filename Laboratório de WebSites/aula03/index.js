document.getElementById('texto1').innerHTML = `Valor de (8 * 3 + 2 / 2): ${8 * 3 + 2 / 2}`, 8 * 3 + 2 / 2;
document.getElementById('texto2').innerHTML = `Valor de (1 + 3 ** 2 / 9): ${1 + 3 ** 2 / 9}`;
document.getElementById('texto3').innerHTML = `Valor de (1 + 3 ** 2 / 9): ${1 + 3 ** 2 / 9}`;
document.getElementById('texto4').innerHTML = `Valor de (-3 + 4 * (10 % 4): ${-3 + 4 * (10 % 4)}`;
document.getElementById('texto5').innerHTML = `Valor de (8 - 2 * 3) % 1 * 2: ${(8 - 2 * 3) % 1 * 2}`;


function acao1(){
    document.getElementById('frase1').innerHTML = "Você clicou no 1° botão";
}

function acao2(){
    document.getElementById('frase2').innerHTML = "Você clicou no 2° botão";
}

function acao3(){
    document.getElementById('frase3').innerHTML = "Você clicou no 3° botão";
}

function acao4(){
    document.getElementById('frase4').innerHTML = "Você clicou no 4° botão";
}


function calcular(){
    let valor_user, total_dobro, total_metade;
    valor_user = prompt("Digite o valor: ");
    total_dobro = valor_user * 2;
    total_metade = valor_user / 2;

    document.getElementById("metade").innerHTML = `Metade de ${valor_user} é ${total_metade}`;
    document.getElementById("dobro").innerHTML = `Dobro de ${valor_user} é ${total_dobro}`;
}






