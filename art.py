suits = {
      "spades": "♠",
      "diamonds": "♦",
      "hearts": "♥",
      "clubs": "♣"
}

values = {
      "ace": "A",
      "king": "K",
      "queen": "Q",
      "jack": "J",
      "ten": "10",
      "nine": "9",
      "eight": "8",
      "seven": "7",
      "six": "6",
      "five": "5",
      "four": "4",
      "three": "3",
      "two": "2"
}

logo = """.------.            _     _            _    _            _     
|A_  _ |.          | |   | |          | |  (_)          | |    
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __ 
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / 
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <  
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\ 
      |  \/ K|                            _/ |                 
      `------'                           |__/                  """
_Card = [
".---------.",
"|C        |",
"|         |",
"|    S    |",
"|         |",
"|        C|",
"`---------`"
] 

_Hidden_Card = [
".---------.",
"|/\/\/\/\/|",
"|\/\/\/\/\|",
"|/\/\/\/\/|",
"|\/\/\/\/\|",
"|/\/\/\/\/|",
"`---------`"
] 

DividerOne = "---------------------------------------------------------------"

DividerTwo = "***************************************************************"

cardWidth = 11
cardHeight = 7

def get_Card_Art(cardValue, cardSuit, cardHidden):
      if cardHidden == True:
            new_Card = _Hidden_Card.copy()
      else:
            new_Card = _Card.copy()
            # Replace the cards value
            card_Value = values[cardValue.lower()]
            if len(card_Value) == 2:
                  new_Card[1] = f"|{card_Value}       |"
                  new_Card[5] = f"|       {card_Value}|"
            else:
                  new_Card[1] = f"|{card_Value}        |"
                  new_Card[5] = f"|        {card_Value}|"

            # Replace card suit
            card_suit = suits[cardSuit.lower()]
            new_Card[3] = f"|    {card_suit}    |"

      return new_Card


            
