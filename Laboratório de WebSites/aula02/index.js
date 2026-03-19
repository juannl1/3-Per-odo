function saudacao1(){
    let nome, idade, sobrenome;
    nome = prompt('Nome: ');
    sobrenome = prompt('Sobrenome: ');
    idade = prompt('Idade: ');

    alert(`SEUS DADOS FORAM VAZADOS !!!!!!!!!!!!! \n\n${nome} ${sobrenome} \nVocê tem ${idade} anos de idade.`);
}

function saudacao2(){
    let nome = prompt('Nome: ') || "Convidado";
    let res = document.getElementById('resultado')
    res.innerHTML = `Olá ${nome} \nBem vindo ao painel`
    
}
function calculo(){
    let valor2 = prompt('valor 1');
    let valor1 = prompt('valor 2');
    let res = document.getElementById('resultado')
}