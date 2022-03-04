from random import choice
from forca import *

header('Jogo da Forca')

#Leitura do arquivo words
word_list = []
file = open('words', 'r')
for line in file:
    line = line.strip()
    word_list.append(line)
file.close()

#Sorteio da palavra que sera impressa
secret_word = choice(word_list)

#Troca do "_" para letras acertadas e imprime o numero de letras da palavra sorteada
line = ["_" for letter in secret_word]
print(f'Número de letras {len(line)}')

mistake = 0
while True:
  player = input('Qual a letra?: ').lower().strip()
  position = 0

  if player not in secret_word: #Contabilizar a quantidade de erros
      mistake += 1
      if mistake < 6:
        print('\033[0;31mERROU! Tente Novamente\033[m')
      forca(mistake)

  for letter in secret_word: #Ira listar as letras da palavra sorteada e comparar com as letras digitadas
    if player == letter:
      line[position] = letter
    position += 1

  if "_" not in line: #Verifica se ainda falta advinhar mais alguma letra
    print(line)
    print('\033[0;32mParabens!! Você venceu!!\033[m')
    break

  if mistake == 6: #Limita o numero de erros
    print(game_over())
    break
  print(line)
