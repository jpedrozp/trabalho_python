# Questão 02 - Escreva um programa em Python que lê uma sequência de dígitos, sendo cada um dos dígitos fornecido numa linha separada, e 
# calcula o número inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a sequência de dígitos é fornecido ao programa o inteiro −1.
# Por exemplo, lendo os dígitos 1 5 4 5 8, o programa calcula o número inteiro 15458.

calculo = 0
while True:
  try:
    numero = int(input('Digite um número: ')) 
    if (numero == -1):
      break
    calculo = calculo * 10 + numero
  except ValueError:
    print('Erro. Digite um valor válido!')
print('O número é: ', calculo)
