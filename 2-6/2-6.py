"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
Site: https://python.nilo.pro.br/
Arquivo: Arquivo: exercicios3\capitulo 02\exercicio-02-06.py


Modifique o Programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750.

"""

# 1 
salario1 = 750
aumento1 = 15/100

salario_novo1 = salario1 + salario1 * aumento1
print (f"O novo salário é de: {salario_novo1}")

# 2
salario2 = 750
aumento2 = 0.15

salario_novo2 = salario2 + salario2 * aumento2
print (f"O novo salário é de: {salario_novo2}")

# 3
salario3 = 750
aumento3 = 15

salario_novo3 = salario3 + ( salario3 * aumento3 / 100)
print (f"O novo salário é de: {salario_novo3}")
