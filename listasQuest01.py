# Questão 01 - Neste exercício, você criará um programa que lê palavras do usuário até que o usuário entre com uma linha em branco.
# Após o usuário digitar uma linha em branco, seu programa deve exibir cada palavra inseridapelo usuário exatamente uma vez. 
# As palavras devem ser exibidas em na mesma ordem em que foram inseridos. Por exemplo, se o usuário digitar:
# primeiro
# segundo
# primeiro
# terceiro
# segundo
# então seu programa deve exibir:
# primeiro
# segundo
# terceiro

lista = []
while True:
  palavras = input('Digite uma palavra (Linha em branco para parar): ')
  set_lista = list(set(lista))
  if palavras == '':
    set_lista.sort()
    break
  lista.append(palavras)
for i, linguagem in enumerate(set_lista):
    print("-->", linguagem)
