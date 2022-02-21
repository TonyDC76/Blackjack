import art
import game

# myCard = art.get_Card_Art("ace", "DiAmOnDs", True)
# myCards = [
#     {
#         "Suit": "Diamonds",
#         "ValueName": "Ten",
#         "Value": 10,
#         "Hidden": False
#     },
#     {
#         "Suit": "Clubs",
#         "ValueName": "Nine",
#         "Value": 9,
#         "Hidden": False
#     }
# ]


# cardPair = []
# cardOne = art.get_Card_Art(myCards[0]["ValueName"],myCards[0]["Suit"],myCards[0]["Hidden"])
# cardTwo = art.get_Card_Art(myCards[1]["ValueName"],myCards[1]["Suit"],myCards[1]["Hidden"])
# for counter in range(art.cardHeight):
#     cardPair.append(cardOne[counter] + "  " + cardTwo[counter]) 

# for line in cardPair:
#     print(line)

game.reset_card_pool()
game.show_cards()
