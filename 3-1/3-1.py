"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
Site: https://python.nilo.pro.br/
Arquivo: Arquivo: exercicios3\capitulo 03\exercicio-03-01.py

Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.

    Número          Tipo numérico
    5           inteiro ○u ponto flutuante
    5.0         inteiro ○u ponto flutuante
    4.3         inteiro ○u ponto flutuante
    -2          inteiro ○u ponto flutuante
    100         inteiro ○u ponto flutuante
    1.333       inteiro ○u ponto flutuante


"""

dados_exercicio = [5, 5.0, 4.3, -2, 100, 1.333]


print(f"\n O número 5 é do tipo: {type(dados_exercicio[0])}")

print(f"\n O número 5.0 é do tipo: {type(dados_exercicio[1])}")

print(f"\n O número 4.3 é do tipo: {type(dados_exercicio[2])}")

print(f"\n O número -2 é do tipo: {type(dados_exercicio[3])}")

print(f"\n O número 100 é do tipo: {type(dados_exercicio[4])}")

print(f"\n O número 1.333 é do tipo: {type(dados_exercicio[5])}\n")
