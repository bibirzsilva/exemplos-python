import random

pkm_meu = "Charmander"
pkm_rival = "Blastoise"

vida_char = 100
vida_blas = 100

print(f"--- BATALHA: {pkm_meu} vs {pkm_rival} ---")

while vida_char > 0 and vida_blas > 0:
    
    print(f"\nSeu {pkm_meu}: {vida_char} HP | Inimigo {pkm_rival}: {vida_blas} HP")
    print("Escolha: 1- Atacar | 2- Curar | 3- Fugir")
    
    opc = input("O que você vai fazer? ")

    if opc == "1":
        dano = random.randint(15, 25)
        vida_blas = vida_blas - dano
        print(f"Boa! Você tirou {dano} de vida do {pkm_rival}!")
        
    elif opc == "2":
        cura = random.randint(10, 20)
        vida_char = vida_char + cura
        print(f"Ufa! Você recuperou {cura} de vida.")
        
    elif opc == "3":
        print("Você correu da luta!")
        break
        
    else:
        print("Opção inválida! Perdeu o turno.")

    if vida_blas <= 0:
        vida_blas = 0
        print(f"O {pkm_rival} desmaiou! Você venceu!")
        break

    print(f"\nO {pkm_rival} está atacando...")
    dano_dele = random.randint(12, 20)
    vida_char = vida_char - dano_dele
    print(f"Vixe! Ele te deu {dano_dele} de dano.")

    if vida_char <= 0:
        vida_char = 0
        print(f"Seu {pkm_meu} foi derrotado...")

print("\n--- FIM DE JOGO ---")