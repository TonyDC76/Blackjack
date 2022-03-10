from glob import glob
import random
import os
import art

# Debug Mode flag, to disable set to False
_debugMode = False



cardPool = []
playerCards = []
computerCards = []
PlayerName = ""
playerCardsValue = 0
computerCardsValue = 0
remainingCards = 0
cardPoolIsReset = False
num_of_decks = 4

suits = ["diamonds", "hearts", "clubs", "spades"]    

cards_in_suits = {
    "ace": 11, 
    "king": 10, 
    "queen": 10, 
    "jack": 10, 
    "ten": 10 , 
    "nine": 9, 
    "eight": 8, 
    "seven": 7, 
    "six": 6, 
    "five": 5, 
    "four": 4, 
    "three": 3, 
    "two": 2
    }

def get_terminal_width():
    t_col, t_Lines = os.get_terminal_size()
    return int(t_col)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_text_centered(textToPrint):

    term_width = get_terminal_width()

    if type(textToPrint) == str:
        # Convert Multi-Line strings into a list
        newTextToPrint = textToPrint.split("\n")
        textToPrint = newTextToPrint

    for item in textToPrint:
        print(item.center(term_width))


def get_player_cards_artwork(PlayerType):

    # Get each of the cards for the specified player and combine them into one artwork
    # List that can then be printed line by line by the print_text_centered function. 
    # This combines all cards a player has side by side for display.

    cardGroup = []
    cards = []
    
    if PlayerType == "Human":
        for x in range(0, len(playerCards)):
            cards.append(art.get_Card_Art(playerCards[x]["ValueName"],playerCards[x]["Suit"],playerCards[x]["Hidden"]))
    else:
        for x in range(0, len(computerCards)):
            cards.append(art.get_Card_Art(computerCards[x]["ValueName"],computerCards[x]["Suit"],computerCards[x]["Hidden"]))
    
    for counter in range(art.cardHeight):
        for x in range(0, len(cards)):
            if x == 0:
                totalCardArtLine = cards[x][counter]
            else:
                totalCardArtLine += " " + cards[x][counter]
    
        cardGroup.append(totalCardArtLine)
    
    return cardGroup


def reset_card_pool():

    #Init or reset the pool of available cards

    global remainingCards
    global cardPoolIsReset

    cardPool.clear()

    for count in range(num_of_decks):
        for suit in suits:
            for key in cards_in_suits.keys():
                cardPool.append(
                    {
                        "Suit": suit,
                        "ValueName": key,
                        "Value": cards_in_suits[key]
                    }
                )
    random.shuffle(cardPool)
    remainingCards = len(cardPool)
    cardPoolIsReset = True


def deal_card():

    #Randomly select a card from the card pool, remove it from the pool and return it.

    global remainingCards

    selectedCardIdx = random.randint(0, len(cardPool) -1)
    selectedCard = cardPool[selectedCardIdx]
    cardPool.pop(selectedCardIdx)
    return selectedCard.copy()
    remainingCards = len(cardPool)


def resetPlayerCards():

    #Reset all players initial cards

    global playerCards
    global computerCards
    global computerCardsValue
    global playerCardsValue

    playerCards.clear()
    computerCards.clear()
    computerCardsValue = 0
    playerCardsValue = 0


def deal_initial_cards():

    #Deal players their initial two cards, 2 cards each with one for the dealer remaining hidden

    # Check the number of remaining cards, if 25% or less of the original number then shuffle the decks
    
    global remainingCards

    if remainingCards <= int((num_of_decks * 52) * (25/100)):
        reset_card_pool()

       
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", False)
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", True)


def deal_card_to_player(playerType, HiddenCard):

    #Deal a card to the specifid player, accepts player types of Human or Computer

    global remainingCards

    if playerType == "Human":
        newCard = deal_card()
        playerCards.append(
            {
                "Suit": newCard["Suit"],
                "ValueName": newCard["ValueName"],
                "Value": newCard["Value"],
                "Hidden": HiddenCard
            }
        )
    else:
        newCard = deal_card()
        computerCards.append(
            {
                "Suit": newCard["Suit"],
                "ValueName": newCard["ValueName"],
                "Value": newCard["Value"],
                "Hidden": HiddenCard
            }
        )

    remainingCards = len(cardPool)

def print_game_art():

    # Prints the game artwork to the console

    global playerCardsValue
    global computerCardsValue
    global cardPoolIsReset

    global _debugMode

    playerCardsValue = get_card_values("Human")
    computerCardsValue = get_card_values("Computer")

    # Clear the screen and print game header artwork
    clearConsole()
    print_text_centered(art.DividerTwo)
    print_text_centered(art.logo)
    print_text_centered(art.DividerTwo)

    if cardPoolIsReset:
        print_text_centered(f"Cards have been Shuffled!\n")
        cardPoolIsReset = False
    else:
        if _debugMode:
            print_text_centered(f"Cards Ramining: {remainingCards}\n")
        else:
            print("\n")


    print_text_centered(art.DividerOne)
    print_text_centered("Dealer")
    print_text_centered(art.DividerOne)
    print("\n")
    print_text_centered(get_player_cards_artwork("Computer"))
    print_text_centered(f"Score: {computerCardsValue}")
    print("\n")
    print_text_centered(art.DividerOne)
    print_text_centered(PlayerName)
    print_text_centered(art.DividerOne)
    print("\n")
    print_text_centered(get_player_cards_artwork("Human"))
    print_text_centered(f"Score: {playerCardsValue}")


def get_card_values(PlayerType):

    # Determine the value of the cards in a players hand accounting for
    # Ace value being either 11 or 1, and the dealer having hidden cards

    # TODO 1:
    # Optimise logic, currently a single Ace will show a value of 1 where it should show 11
    # Rework logic and refactor code


    totalValue = 0
    numOfAces = 0
    HiddenCard = False

    if PlayerType == "Human":
        cardsToCheck = playerCards
    else:
        cardsToCheck = computerCards


    # Get the number of ACE's
    numOfAces = 0
    for card in cardsToCheck:
        if card["Hidden"]:
            HiddenCard = True

        if (card["ValueName"] == "ace" and HiddenCard == False):
            numOfAces += 1
        else:
            # Get total of Non-Ace cards
            if not HiddenCard:
                totalValue += card["Value"]


    if totalValue == 10 and numOfAces == 1:
        totalValue = 21
    elif totalValue == 10 and numOfAces > 1:
        totalValue = 10 + numOfAces 
    elif totalValue >= 10:
        totalValue += numOfAces
    else:
        if totalValue <=9 and numOfAces == 2:
            totalValue += 12
        elif (numOfAces >= 1 and (totalValue + numOfAces <= 10 and not HiddenCard)):
            totalValue = totalValue + 11 + (numOfAces -1)
        else: 
            totalValue = totalValue + numOfAces

    return totalValue


def play_blackjack():

    global PlayerName
    global playerCardsValue
    global computerCardsValue

    winnerOfGame = ""
    sel = ""

    resetPlayerCards()
    clearConsole()

    deal_initial_cards()
    playerCardsValue = get_card_values("Human")
    computerCardsValue = get_card_values("Computer")
    print_game_art()


    GameIsOver = False
    while (not GameIsOver):

        PlayerTurn = "Human"
        while (PlayerTurn == "Human"):
            
            sel = ""
            playerCardsValue = get_card_values("Human")
            computerCardsValue = get_card_values("Computer")

            if playerCardsValue == 21:
                PlayerTurn = "Computer"
            elif playerCardsValue >= 22:
                winnerOfGame = "Computer"
                PlayerTurn = "Computer"
            else:
                while (sel.upper() != "H" and sel.upper() != "S"):
                    sel = input("Please select either 'H' for Hit or 'S' to Sit: ")
                    if sel.upper() != "H" and sel.upper() != "S":
                        print("You have selected an invalid option, please try again!")
                
                if sel.upper() == "S":
                    PlayerTurn = "Computer"
                else:
                    deal_card_to_player("Human", False)
                    print_game_art()


        while (not GameIsOver):

            computerCards[1]["Hidden"] = False
            print_game_art()

            if playerCardsValue <= 21:

                if computerCardsValue <= 16:
                    deal_card_to_player("Computer", False)
                    print_game_art()
                else:
                    GameIsOver = True
            else:
                GameIsOver = True

    if computerCardsValue == 21:
        if playerCardsValue == 21:
            winnerOfGame = "Draw"
        else:
            winnerOfGame = "Computer"
    elif (computerCardsValue <=21 and playerCardsValue <= 21) and ((playerCardsValue == computerCardsValue)):
        winnerOfGame = "Draw"
    elif playerCardsValue <= 21 and ((playerCardsValue > computerCardsValue) or computerCardsValue > 21):
        winnerOfGame = "Human"
    else:
        winnerOfGame = "Computer"


    if winnerOfGame == "Computer":
        print_text_centered("\nYOU LOSE!")
    elif winnerOfGame == "Human":
        print_text_centered("\nYOU WIN!")
    else:
        print_text_centered("\nIt is a Draw!")