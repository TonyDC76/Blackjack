import random
import os
import art

cardPool = []
playerCards = []
computerCards = []
PlayerName = ""

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


def deal_initial_cards():
    
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", False)
    deal_card_to_player("Human", False)
    deal_card_to_player("Computer", True)
    

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
    print("\n")
    print_text_centered(art.DividerOne)
    print_text_centered(PlayerName)
    print_text_centered(art.DividerOne)
    print("\n")
    print_text_centered(get_player_cards_artwork("Human"))


def get_card_values(PlayerType):

    totalValue = 0

    if PlayerType == "Human":
        cardsToCheck = playerCards
    else:
        cardsToCheck = computerCards

    # Get the number of ACE's
    numOfAces = 0
    for card in cardsToCheck:
        if card["ValueName"] == "ace":
            numOfAces += 1
        else:
            # Get total of Non-Ace cards
            totalValue += card["Value"]

    print(totalValue)

def play_blackjack():

    global PlayerName
    clearConsole()
    #PlayerName = input("Please enter your name: ")
    PlayerName = "Player 1"

    deal_initial_cards()
    print_game_art()


    GameIsOver = False
    while (not GameIsOver):

        PlayerTurn = "Human"
        while (PlayerTurn == "Human"):
            
            get_card_values("Human")
