# Conversor de números reais para binário

- Used Language: Python
- Note: Não é permitido usar nenhuma biblioteca de Python específica para essa conversão
- Obs.: Foram feitos dois códigos, a lógica para criar o algoritmo é a mesma, a mudança está no fato de que o programa `convNreais_2.py` possui um laço `while()`, o que permite que, caso o usuário tenha digitado um valor inválido a inserção de um outro valor seja possivel, isso já não acontece no programa `convNreais.py`, caso o número digitado pelo usuário seja inválido o programa finaliza, mostrando uma mensagem de erro.

## Descrição do Projeto

Escreva um programa em `Python 3` que leia um número real no intervalo aberto (0, 1) e gere suas representações em binário com diferentes precisões (quantidade de bits), começando com `5 bits` e indo até `16 bits`, de um em um. A saída deve ser apresentada conforme o modelo abaixo. O erro deve ser mostrado em porcentagem e com 4 casas decimais.

## Exemplo de saída do programa

Nome do Projeto: Conversor de números reais para binário

Dado de entrada = 0.23
Resultados

Com 5 bits

- Aproximação a menor: 0.00111 -> 0.21875 com erro = 4.891%
- Aproximação a maior: 0.01000 -> 0.25 com erro = 8.696%

Com 6 bits

- Aproximação a menor: 0.001110 -> 0.21875 com erro = 4.891%
- Aproximação a maior: 0.001111 -> 0.234375 com erro = 1.902%

Com 7 bits

- Aproximação a menor: 0.0011101 -> 0.2265625 com erro = 1.495%
- Aproximação a maior: 0.0011110 -> 0.234375 com erro = 1.902%

Com 8 bits

- Aproximação a menor: 0.00111010 -> 0.2265625 com erro = 1.495%
- Aproximação a maior: 0.00111011 -> 0.23046875 com erro = 0.204%

Com 9 bits

- Aproximação a menor: 0.001110101 -> 0.228515625 com erro = 0.645%
- Aproximação a maior: 0.001110110 -> 0.23046875 com erro = 0.204%

Com 10 bits

- Aproximação a menor: 0.0011101011 -> 0.2294921875 com erro = 0.221%
- Aproximação a maior: 0.0011101100 -> 0.23046875 com erro = 0.204%

Com 11 bits

- Aproximação a menor: 0.00111010111 -> 0.22998046875 com erro = 0.008%
- Aproximação a maior: 0.00111011000 -> 0.23046875 com erro = 0.204%

Com 12 bits

- Aproximação a menor: 0.001110101110 -> 0.22998046875 com erro = 0.008%
- Aproximação a maior: 0.001110101111 -> 0.230224609375 com erro = 0.098%

Com 13 bits

- Aproximação a menor: 0.0011101011100 -> 0.22998046875 com erro = 0.008%
- Aproximação a maior: 0.0011101011101 -> 0.2301025390625 com erro = 0.045%

Com 14 bits

- Aproximação a menor: 0.00111010111000 -> 0.22998046875 com erro = 0.008%
- Aproximação a maior: 0.00111010111001 -> 0.23004150390625 com erro = 0.018%

Com 15 bits

- Aproximação a menor: 0.001110101110000 -> 0.22998046875 com erro = 0.008%
- Aproximação a maior: 0.001110101110001 -> 0.230010986328125 com erro = 0.005%

Com 16 bits

- Aproximação a menor: 0.0011101011100001 -> 0.2299957275390625 com erro = 0.002%
- Aproximação a maior: 0.0011101011100010 -> 0.230010986328125 com erro = 0.005%
