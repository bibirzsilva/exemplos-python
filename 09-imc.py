import os
os.system("cls")
 
peso = float(input("Coloque o seu peso Por favor: "))
altura = float(input("Coloque a sua altura Por favor: "))
imc = peso / (altura * altura)
print("Seu Imc Será: ",imc)