import os
os.system

def dividir_conta(total, pessoas):
    return total / pessoas

print("Seja bem vindo ao App Minha Conta!")

valor_total = float(input("Informe o valor da conta: "))
quantidade_pessoas = int(input("Digite o número de pessoas: "))

print("\n==== Pressione Enter para calcular ====")
input() # Pausa para o usuário

resultado = dividir_conta(valor_total, quantidade_pessoas)

print(f"Total da conta: R$ {valor_total:.2f}")
print(f"Número de Pessoas: {quantidade_pessoas}")
print(f"Valor por pessoa: R$ {resultado:.2f}")