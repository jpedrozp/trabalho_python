# Questão 02 – Escreva um programa em Python que leia 10 conjuntos de dois valores, o primeiro representando 
# Ano e o segundo representando a média de temperatura daquele ano. Encontre a temperatura mais alta e a mais baixa. 
# Mostre o ano da mais alta e o ano da mais baixa, junto com sua média.

temp_media = dict()
for i in range(10):
  try:
    ano = int(input('Digite um ano correspondente: '))
    temp_media[ano] = float(input('Digite a média do ano digitado: '))
  except ValueError:
    print('Erro. Digite um valor válido!')

maior_media = ""
menor_media = ""
for ano, nota in temp_media.items():
    if maior_media == "":
        maior_media = ano
    elif menor_media == "":
        menor_media = ano
    elif temp_media[menor_media] > nota:
        menor_media = ano
    elif temp_media[maior_media] < nota:
        maior_media = ano
print('--' *30)
print(f'O ano de maior média foi {maior_media}, e a sua média foi {temp_media[maior_media]} ')
print(f'O ano de menor média foi {menor_media}, e a sua média foi {temp_media[menor_media]}')
