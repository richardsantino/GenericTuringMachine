# GenericTuringMachine
Para executar esse programa em sua maquina, no prompt de comando, possuindo a instalação do python, execute dentro do caminho da pasta desse projeto, o comando:
python main.py

As configurações da Maquina de Turing estão contidas no arquivo input.txt, sendo possivel alterar-las seguindo as regras:

1. Na primeira linha, os sımbolos do alfabeto de entrada (Σ), com letras sempre em minusculo e sem espa¸cos
em branco entre os sımbolos, concatenados com sımbolos do alfabeto fita (Γ), sem o s´ımbolo em branco t,
considere que teremos no maximo 30 sımbolos na primeira linha.

2. Na segunda linha, o numero de estados, para facilitar a implementação o estado de aceitação sempre sera
o ultimo estado, considere tambem que o estado inicial sera sempre o primeiro estado e qualquer maquina tera no maximo 50 estados.

3. Na terceira linha, o numero de n transições da maquina e nas proximas n linhas seguem as transições especificadas no seguinte formato, separadas por espaço em branco:
<estado corrente> branco <sımbolo em Γ > branco <gravar na fita> branco <mover> branco <estado chegada>
onde as ações de mover a cabeça de leitura são representadas pelas letras E (move para a esquerda), D(move para a direita). O sımbolo em branco t sera representado pelo caractere − (hifen).
  
4. Ao final das n transições, teremos uma linha com um inteiro especificando o numero de palavras que deverão ser testadas na maquina de Turing, as palavras estão armazenadas na fita da maquina e não conterão espaços em branco e estarão cada uma em uma linha contendo os simbolos do alfabeto de entrada (Σ). Considere tambem, que a fita tera no maximo 100 caracteres.
