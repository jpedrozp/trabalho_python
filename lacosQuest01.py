# Questão 01 - Escreva um programa em Python que pede ao utilizador que lhe forneça um inteiro correspondente a um número de segundos e que 
# calcula o número de dias correspondentes a esse número de segundos. O número de dias é fornecido como um real. O programa termina quando o utilizador 
# fornece um número negativo.

while True:
  try:
    valor = int(input('Digite um número de segundos ou um número negativo para terminar --> '))
    if valor < 0:
        print('Encerrado :)')
        break    
    print('O número de dias correspondente é --> ', valor/86400)
  except ValueError:
    print('Erro. Digite um valor válido!')
