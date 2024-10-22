const botao = document.getElementById('btn');
const input = document.getElementById('input');

botao.addEventListener('click', verificarValor);

function verificarValor() {
    const valor = parseFloat(input.value); // Pega o valor do input e converte para número
    const valorComparacao = 4000; // Valor de comparação

    // Verifica se o valor é um número válido
    if (isNaN(valor)) {
        console.log('Por favor, insira um número válido.');
    } else if (valor > valorComparacao) {
        console.log(`O valor ${valor} é maior que ${valorComparacao}.`);
    } else {
        console.log(`O valor ${valor} NÃO é maior que ${valorComparacao}.`);
    }
}
