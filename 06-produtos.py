import os
os.system("cls")
 
item = str(input("Qual o Nome do Produto Comprado: "))
quant = int(input("Quantos Foram comprados: "))
valor = int(input("Insira o Valor do Produto: "))
 
valor = valor * quant
 
if quant <= 5:    
    valor = valor - (valor /100 * 2 )
if quant <= 10:
     valor = valor - (valor / 100 * 3)
if quant > 10:
     valor = valor - (valor / 100 * 5)
 
print("A compra de",item)
print(f"Irá custar: {valor:.2f}")

