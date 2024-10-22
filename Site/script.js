const botao = document.getElementById('btn');
const input = document.getElementById('input');
const message = document.getElementById('message');  // Referência para a div da mensagem

botao.addEventListener('click', verificarValor);

function verificarValor() {
    const valor = parseFloat(input.value); // Pega o valor do input e converte para número
    const valorComparacao = 4000; // Valor de comparação

    // Verifica se o valor é um número válido
    if (isNaN(valor)) {
        message.innerHTML = '<p class="text-danger">Por favor, insira um número válido.</p>';
    } else if (valor >= valorComparacao) {
        message.innerHTML = `<p class="text-success">Parabéns! Seu lance de R$ ${valor.toFixed(2)} foi aceito.</p>`;
    } else {
        message.innerHTML = `<p class="text-danger">O valor do lance precisa ser no mínimo R$ ${valorComparacao.toFixed(2)}.</p>`;
    }
}
