import random

while True:
    choices = ["batu","kertas","gunting"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("batu, kertas, or gunting?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Seri!")

    elif player == "batu":
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("Yhahha Kalah!")
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("Menang cuy")

    elif player == "gunting":
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("Yhahha Kalah!")
        if computer == "kertas":
            print("computer: ", computer)
            print("player: ", player)
            print("Menang cuy")

    elif player == "kertas":
        if computer == "gunting":
            print("computer: ", computer)
            print("player: ", player)
            print("Yhahha Kalah!")
        if computer == "batu":
            print("computer: ", computer)
            print("player: ", player)
            print("Menang cuy")

    play_again = input("Main Lagi? (iyh/g): ").lower()

    if play_again != "iyh":
        break

print("dadah!")
# ****************************************************************