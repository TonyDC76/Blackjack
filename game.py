import random

cardPool = []
playerHands = []
computerCards = []


def reset_card_pool():

    num_of_decks = 4
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    
    cards_in_suits = {
        "Ace": 11, 
        "King": 10, 
        "Queen": 10, 
        "Jack": 10, 
        "Ten": 10 , 
        "Nine": 9, 
        "Eight": 8, 
        "Seven": 7, 
        "Six": 6, 
        "Five": 5, 
        "Four": 4, 
        "Three": 3, 
        "Two": 2
        }
 
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
    
def show_cards():
    for card in cardPool:
        s = card["Suit"]
        v = card["ValueName"]
        print(f"{v} of {s}")
    print(f"Total Cards: {len(cardPool)}")