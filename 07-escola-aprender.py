import os
os.system("cls")
nome = str(input("Qual o seu Nome? "))
genero = int(input("Você é um Homem ou Mulher, Digite 1 para Mulher 2 para Homem: "))
if genero == 1:
    print("Ola Senhora",nome)
nivel = int(input("Qual o Seu nivel de Professor insira do 1 ao 3: "))
aulas = int(input("Quantas Aulas Lecionou essa Semana: "))
if genero == 2:
    print("Ola Senhor",nome)
nivel = int(input("Qual o Seu nivel de Professor insira do 1 ao 3: "))
aulas = int(input("Quantas Aulas Lecionou essa Semana: "))
 
if nivel == 1:
    salario = 12 * aulas
    print("O seu salario será: ",salario)
if nivel == 2:
    salario = 17 * aulas
    print ("O seu salario será: ",salario)
if nivel == 3:
    salario = 25 * aulas
    print ("O seu salario será: ",salario)