// primeira parte
function primeira_funcao(){

    let x = prompt("Digite sua idade: ");
    
    let y = 10;
    let z = "*Sonho*";
    document.getElementById("frase").innerHTML = `Você tem <b>${x}</b> de idade, seu sonho é <b>${z}</b> e ele se realizará em <b>${y}</b>`;
    
    document.getElementById("variaveis").innerHTML = `Variaveis utilizadas: <b>${x}, ${y}</b> e <b>${z}</b>`
}

// Término da primeira parte


// segunda parte


function verificacao_de_idade(){
    let idade = prompt("Digite sua idade");
    
    if (idade >= 16 && idade <= 17){
        document.getElementById("texto_de_saida_eleicao").innerHTML = `Você pode votar já pode votar`;

        document.getElementById("idade").innerHTML = `Idade: <b>${idade}</b>`;

    } else if (idade >= 18 && idade < 65) {
        document.getElementById("texto_de_saida_eleicao").innerHTML = `Seu voto é obrigatório`;

        document.getElementById("idade").innerHTML = `Idade: <b>${idade}</b>`;

    } else if (idade >= 65) {
        document.getElementById("texto_de_saida_eleicao").innerHTML = `Seu voto é optativo`;

        document.getElementById("idade").innerHTML = `Idade: <b>${idade}</b>`;
    }

    else {
        document.getElementById("texto_de_saida_eleicao").innerHTML = `Você <b>NÃO</b> pode votar`;
        document.getElementById("idade").innerHTML = `Idade: <b>${idade}</b>`;
    }
}



function verificacao_de_idade_cnh(){
    let idade = prompt();

    if (idade < 16){
        document.getElementById("texto_de_saida_cnh").innerHTML = `Você não pode dirigir nos EUA`;

        document.getElementById("idade_cnh").innerHTML = `Idade: <b>${idade}</b>`;
    } else if (idade >= 16 && idade > 149){
        document.getElementById("texto_de_saida_cnh").innerHTML = `Você pode dirigir nos EUA`;

        document.getElementById("idade_cnh").innerHTML = `Idade: <b>${idade}</b>`;
    } else {
        document.getElementById("texto_de_saida_cnh").innerHTML = `Idade inválida`;
    }
}


function verificar_dia_da_semana(){
    let dia_da_semana;
    let perguntando_dia_da_semana = prompt("ex: \n1. Domingo \n2. Segunda\n\nDigite o dia da semana: ");

    switch (perguntando_dia_da_semana - 1) {
        case 0:
            dia_da_semana = "<b>Domingão</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana}. Amanhã tem que trabalhar -_-`;
            break

        case 1:
            dia_da_semana = "<b>Segunda-Feira</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana}. Começou tudo de novo -_-`;
            break

        case 2:
            dia_da_semana = "<b>Terça-Feira</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana} ta longe do final de semana`;
            break

        case 3:
            dia_da_semana = "<b>Quarta-Feira</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana} Meio de semana :|`;
            break

        case 4:
            dia_da_semana = "<b>Quinta-Feira</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana} Ta quase :)`;
            break
        case 5:
            dia_da_semana = "<b>Sexta-Feira</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana} SEXTAAAAAAA!!!!!!! :)`;
            break
        
        case 6:
            dia_da_semana = "<b>Sábadão</b>"
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = `Hoje é: ${dia_da_semana} Finalmente chegou o dia de aproveitar`;
            break
        default:
            document.getElementById("texto_de_saida_dia_da_semana").innerHTML = ("Você não digitou um dia válido");

    }
            
}


