"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
Site: https://python.nilo.pro.br/
Arquivo: exercicios3\capitulo 02\exercicio-02-02.py

Digite a seguinte expressão no interpretador:
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das operações é importante.
"""

calculo = 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
print (calculo)

# Primeiro: resolve-se potencialização
calculo_1 = 10 % 3 * 100 + 1 - 10 * 4 / 2
print (f"Cálculo final após primeiro cálculo: {calculo_1}")
print (type(calculo_1))

# Segundo:   resolve-se o módulo
## O operador resto (modulus)(%) trabalha em inteiros (e em expressões inteiras) e fornece o resto da divisão inteira do primeiro operando pelo segundo
calculo_2 = 1 * 100 + 1 - 10 * 4 / 2
print (f"Cálculo final após segundo cálculo: {calculo_2}")
print (type(calculo_2))

# Terceiro: resolve-se multiplicação/divisão seguindo a ordem da esquerda para direita
calculo_3 = 100 + 1 - 10 * 4 / 2
print (f"Cálculo final após terceiro cálculo: {calculo_3}")
print (type(calculo_3))

# Quarto: resolve-se multiplicação/divisão seguindo a ordem da esquerda para direita
calculo_4 = 100 + 1 - 40 / 2
print (f"Cálculo final após quarto cálculo: {calculo_4}")
print (type(calculo_4))

# Quinto: resolve-se multiplicação/divisão seguindo a ordem da esquerda para direita
calculo_5 = 100 + 1 - 20
print (f"Cálculo final após quinto cálculo: {calculo_5}")
print (type(calculo_5))

# Sexto: resolve-se adição/subtração seguindo a rodem da esquerda para direita
calculo_6 = 101 - 20
print (f"Cálculo final após sexto cálculo: {calculo_6}")
print (type(calculo_6))

# Sétimo: resolve-se adição/subtração seguindo a rodem da esquerda para direita
calculo_7 = 81
print (f"Cálculo final após sétimo cálculo: {calculo_7}")
print (type(calculo_7))

#  Estudos a parte: 
teste1 = 1 + 10
print (type(teste1))

teste2 = 1.1 + 10
print (type(teste2))

teste3 = 1 + 10.1
print (type(teste3))

# Quando envolve-se operações de multiplicação, divisão e potência o type resultante é "float",
# Quando envolve-se operções de adição e subtração apenas com números inteiros o type resultante é "int",
# Quando envolve-se operações de adição e subtração com números decimais e/ou não inteiros o type resultante é "float"
