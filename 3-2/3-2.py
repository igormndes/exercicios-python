"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
Site: https://python.nilo.pro.br/
Arquivo: Arquivo: exercicios3\capitulo 03\exercicio-03-02.py

Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

Expressões:
Expressão   Resultado      Expressão   Resultado
a == c    ○ True ○ False   b > a     ○ True ○ False
a < b     ○ True ○ False   c >= f    ○ True ○ False
d > b     ○ True ○ False   f >= c    ○ True ○ False
c != f    ○ True ○ False   c <= c    ○ True ○ False
a == b    ○ True ○ False   c <= f    ○ True ○ False
c < d     ○ True ○ False

"""

# Definindo variáveis:

a = 4
b = 10
c = 5.0
d = 1
f = 5

# Definindo as expressões em uma lista:

expressoes = [
    a == c,
    a < b,
    d > b,
    c != f,
    a == b,
    c < d,
    b > a,
    c >= f,
    f >= c,
    c <= c,
    c <= f 
    ]

# Resultado das expressões:

print (f" Resultado das expressões: {expressoes[0:]}")
