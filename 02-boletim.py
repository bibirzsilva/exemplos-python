
import os
os.system("cls")

print ("Seja bem vindo ao Boletim Virtual")

nome = input ("Digite seu nome: ")
nota01 = float(input ("Digite sua primeira nota: "))
nota02 = float(input ("Digite sua segunda nota: "))
nota03 = float(input ("Digite sua terceita nota: "))

media = (nota01 + nota02 + nota03) / 3
print ("Aluno: ", nome, ", sua média foi: ", media)

if(media>=7):
    print("Você foi Aprovado")

elif (media>=4 and media <=6):
    print ("Você está de recuperação")

else:
    print("Você foi Reprovado")