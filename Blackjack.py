import art
import game

StillPlaying = True


game.reset_card_pool()
game.PlayerName = input("Please enter your name: ")

while StillPlaying:
    game.play_blackjack()

    yn = ""

    while yn.upper() != "Y" and yn.upper() != "N":
        yn = input("Would you like to play again? (Y/N): ")
        if yn.upper() != "Y" and yn.upper() != "N":
            print("You have not selected a valid option, please enter 'Y' for Yes or 'N' for No!") 
        
        if yn == "N":
            StillPlaying = False

