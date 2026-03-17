import os
os.system ("cls")
valor01 = int(input("Digite o Pimeiro Valor: "))
valor02 = int(input("Digite o Segundo Valor: "))
calculo = int(input("Digite qual Calculo Deseja, Digite 1 Para Soma, 2 Para Sub, 3 Para Mult, 4 Para Div: "))
soma = valor01 + valor02
sub = valor01 - valor02
mult = valor01 * valor02
div = valor01 / valor02
if calculo == 1:
    print("A Soma desses Valores é: ",soma)
elif calculo == 2:
    ("A Subtração desses Valores é: ",sub)
elif calculo == 3:
    print("A Multiplicação desses Valores é: ",mult)
elif calculo == 4:
    print("A Divisão desses Valores é: ",div)
 
