function cinema() {
    let nome = prompt("Nome: ");
    let idade = prompt("Idade: ")

    let tipo_de_ingresso = 0;
    
    if (idade >= 18 && idade <= 150) {
        let estudante = prompt("Voçê é estudante ? [s/n]: ")

        if (estudante === "s") {
            tipo_de_ingresso = prompt("1. Inteira \n2. Meia \n3. VIP\n\nTipo de Ingresso:")
        } else if (estudante === "n") {
            tipo_de_ingresso = prompt("1. Inteira \n2. VIP \n\nTipo de Ingresso:")
        } else {
            tipo_de_ingresso = "Inválido"
        }
        
    } else if (idade <= 18) {
        tipo_de_ingresso = prompt("1. Inteira \n2. Meia \n3. VIP\n\nTipo de Ingresso:")
    } else {
        document.getElementById()
    }
    
    
}