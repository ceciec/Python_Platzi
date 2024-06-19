import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("Computer: ", computer_wins)
    print("User: ", user_wins)

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
        print("=> No es una opcion valida.")
        continue
    
    rounds += 1
    computer_option = random.choice(options)

    print("\nUser option => ", user_option)
    print("Computer option => ", computer_option)
    
    if user_option == computer_option:
        print("=> Empate!!!")

    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera!")
            print("=> Usuario gana.\n")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("=> Computadora gana.\n")
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra!")
            print("=> Usuario gana.\n")
            user_wins += 1
        else:
            print("Tijera gana a papel!")
            print("=> Computadora gana.\n")
            computer_wins += 1

    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("=> Usuario gana.\n")
            user_wins += 1
        else:
            print("Piedra gana a tijera!")
            print("=> Computadora gana.\n")
            computer_wins += 1

    if computer_wins == 2:
        print("El ganador es la computadora, buena suerte para la proxima!")
        break

    if user_wins == 2:
        print("GANASTE!!! FELICIDADES...")
        break