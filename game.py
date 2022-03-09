import random
import os
import art

cardPool = []
playerCards = []
computerCards = []
PlayerName = ""
playerCardsValue = 0
computerCardsValue = 0

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
    
#def show_cards():
#     for card in cardPool:
#         s = card["Suit"]
#         v = card["ValueName"]
#         print(f"{v} of {s}")
#     print(f"Total Cards: {len(cardPool)}")



def deal_card():
    selectedCardIdx = random.randint(0, len(cardPool) -1)
    selectedCard = cardPool[selectedCardIdx]
    cardPool.pop(selectedCardIdx)
    return selectedCard.copy()


def resetPlayerCards():

    global playerCards
    global computerCards
    global computerCardsValue
    global playerCardsValue

    playerCards.clear()
    computerCards.clear()
    computerCardsValue = 0
    playerCardsValue = 0

def deal_initial_cards():

       
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", False)
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", True)

    # Debug Code
    #deal_card_to_player("Human", False)

    # global playerCards
    # playerCards.append(
    #     {
    #         "Suit": "Clubs",
    #         "ValueName": "ace",
    #         "Value": 11,
    #         "Hidden": False
    #     }
    # )

def deal_card_to_player(playerType, HiddenCard):

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

def print_game_art():

    global playerCardsValue
    global computerCardsValue

    playerCardsValue = get_card_values("Human")
    computerCardsValue = get_card_values("Computer")

    # Clear the screen and print game header artwork
    clearConsole()
    print_text_centered(art.DividerTwo)
    print_text_centered(art.logo)
    print_text_centered(art.DividerTwo)
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
        if (card["ValueName"] == "ace" and card["Hidden"] == False):
            numOfAces += 1
        else:
            # Get total of Non-Ace cards
            if not card["Hidden"]:
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



            
            
