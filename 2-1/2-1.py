"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
Site: https://python.nilo.pro.br/
Arquivo: exercicios3\capitulo 02\exercicio-02-01.py
Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
10 + 20 × 30
4² ÷ 30
(9^4 + 2) × 6 - 1
"""

calculo_1 = 10 + 20 * 30
print (f"Cálculo 01 :{calculo_1}")

gabarito_1 = 10 + 20 * 30
print (f"Gabarito 01: {gabarito_1} \n")

# para potencializações utilizar **
calculo_2 = 4 ** 2 / 30
print (f"Cálculo 02 :{calculo_2:.2f}")

gabarito_2 = 4 ** 2 / 30 
print (f"Gabarito 02: {gabarito_2:.2f} \n")

calculo_3 = (9 ** 4 + 2) * 6 - 1 
print (f"Cálculo 03 :{calculo_3}")

gabarito_3 = ( 9 ** 4 + 2) * 6  - 1 
print (f"Gabarito 03: {gabarito_3} \n")
