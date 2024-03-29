# -*- coding: utf-8 -*-
"""Exercicios_Funções.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TMAErkBie25tgk-NK90sk-T9hZfz2PKk

1. Cria a função
que reproduza a taboada número n na forma
"""

def taboada(n):
  print(f'Taboada do {n}')
  print('-'*12)
  for m in range(0, 11):
    print(f'{m:2.0f} x {n:2.0f} = {m * n:2.0f}')

taboada(6)

"""2. Implemente uma função que receba um valor n inteiro e imprima até a n-esima linha da seguinte forma:
1
1  2
1  2  3
:  :
1  2  3 ... n
"""

def nesima(n):
  for numero in range(n + 1):
    espaco = ' '
    print(f'{(str(numero) + espaco)* numero} ')

nesima(7)



"""3. Implemente uma função que receba um valor n inteiro e imprima até a n-esima linha da seguinte forma:"""

def nesima(n):
  for n1 in range(n):
    print()
    for n2 in range(n1 + 1):
      print(f'{(str(n2 + 1))}', end=' ')

nesima(5)

"""4. Implemente uma funçâo que receba um valor em segundos e imprima o correspondente em horas, minutos e segundos. Por exemplo, se a função receber com argumento 4814, imprimirá 1 hora(s) 20 minuto(s) e 14 segundo(s)

"""

def conversor(segundos):
  segundos = str(segundos)
  s = 0
  m = 0
  h = 0
  if int(segundos[-2:]) > 59:
    s = int(segundos[-2:]) - 60
  else:
    s = int(segundos[-2:])
  minutos = int(int(segundos) / 60)
  if (int(minutos)) > 59:
    m = minutos - 60
  else:
    m = minutos
  h = int(minutos / 60 )
  print(f'Horas: {h}, Minutos: {m}, Segundos: {s}')


conversor(4814)



"""5. Implemente uma função que retorna True se o argumento de entrada for um número natural primo e False caso contrario."""

def n_primo(numero):
  divi = 0
  for n in range(2, 1000000):
    resultado = numero / n
    resultado = str(resultado)
    if resultado[-1] == '0':
      divi += 1
  if divi > 1:
    return False
  else:
    return True


n_primo(71)

"""6.Implemente uma função que retorne a quantidade de dígitos de um determinado número natural passado como argumento. Por exemplo, ao chamar a função com o número 2131, ela deverá retornar 4.

"""

def quant_digitos(numero):
  quantidade = len(str(numero))
  return quantidade


quant_digitos(2134)

"""7.Implemente a função todos_iguais(sequencia) que retorna True se todos os elementos de sequencia forem iguais, e retorna False caso contrario.

"""

def todos_iguais(sequencia):
  caracteres = set(sequencia)
  if len(caracteres) == 1:
    return True
  else:
    return False


todos_iguais('ccccccccccc')

"""8. implemente a função todos_diferentes(sequencia) que retorna True se todos os elementos de sequencia forem diferentes entre si, e retorna False caso contrario, isto é pelos menos um elemento seja igua a outro componente da sequencia."""

def todos_diferentes(sequencia):
  digitos = len(sequencia)
  caracteres = len(set(sequencia))
  if digitos == caracteres:
    return True
  else:
    return False


todos_diferentes(input('Digite a sequencia: '))

"""9.Implemente uma função que recebe como argumentos um número n e uma lista de números, indice_elemento(n, lista:).A função retornará o indice da primeira ocorrencia do numero na lista e -1 se o número não estiver na lista. Obs: em Python, indices de listas, arrays, etc. começam em 0

"""

def indice_elemento(n, lista):
  indice = -1
  dicionario = {}
  for numero in range(len(lista)):
    dicionario[numero]= lista[numero]
  for k, v in dicionario.items():
    if v == n:
      print(k)
      indice = k
      break
  return indice



lista = [1, 2, 55, 4, 36, 21, 47]
n = int(input('Digite um numero inteiro: '))
indice_elemento(n, lista)

"""10. Implemente uma função que recebe um número n e retorna a menor potencia de 2 maior ou igual a n. Por exemplo, pot2(14) retornará 16, pot2(42) retornará 64.

"""

def pot2(n):
  potencia = 1
  while potencia < n:
    potencia *= 2
  return potencia

pot2(14)

"""11. Implemente uma função que dado um número natural maior do que 1, decomponha esse número em fatores primos. Por exemplo, se o argumento de entrada for 36, a said deverá ser [2,2,3,3], porque 2 X 2 X 3 X 3 = 36.

"""





"""12.Implemnte a função maiorN(lista, N) que recebe uma lista de números quaisquer, um valor N, 1 <= N =len(lista), e retorna o Nésimo maior valor na lista de números. Por exemplo, se N for 1, retorna o maior valor na lista, se N for 2, retorna o segundo maior valor na lista, etc. Exemplo:

lista = [5, -1, 7, 0, -3, 9]
N = 2
print(f'Em {lista) o {N}o. maior valor e {maiorN9(lista, N)}')
"""



