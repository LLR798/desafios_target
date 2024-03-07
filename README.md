# Desafios Target:

Esse repositório faz parte de um desafio técnico de estágio elaborado pela Target. 


## 1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? 

### Resposta:
91

<a href="https://github.com/LLR798/desafios_target/blob/main/codigos/soma.py">
  Código
</a>

## 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

<a href="https://github.com/LLR798/desafios_target/blob/main/codigos/fibonacci.py">
  Código
</a>

## 3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___
9 -> porque está indo de ímpar em ímpar.

b) 2, 4, 8, 16, 32, 64, ____
128 -> porque é o número anterior vezes dois.

c) 0, 1, 4, 9, 16, 25, 36, ____
49 -> porque a soma do próximo é o atual com a soma em ordem crescente somente dos números ímpares.

d) 4, 16, 36, 64, ____
porque a lógica sugere que estamos elevando os número pares a partir do 2 em diante ao quadrado, e o próximo seria o 10 que da 100.

e) 1, 1, 2, 3, 5, 8, ____
porque é igual a sequência de fibonacci, o número anterior mais o atual resulta no próximo.

f) 2,10, 12, 16, 17, 18, 19, ____
porque todos os número começam com a letra D, e próximo depois do dezenove é o duzentos.

## 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

### Resposta:
Podemos ligar um dos interruptores e esperar alguns minutos. Depois desligamos o primeiro e ligamos o segundo interruptor. Vamos até a sala. A lâmpada desligada e quente corresponde ao primeiro interruptor, a lâmpada acesa ao segundo e a lâmpada apagada e fria ao terceiro. Dessa forma conseguimos ir em duas salas e saber qual interruptor pertence a determinada lâmpada.

## 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

<a href="https://github.com/LLR798/desafios_target/blob/main/codigos/inversor_de_string.py">
  Código
</a>