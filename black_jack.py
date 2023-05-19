import random

#blackJack Game.
#Rykers Thoughts on building our game.
    #build a deck
    #have a system to grab random cards.
    #deal cards.
    #option to draw again
    #handle Ace as 1 or 11
    #Bust if over 21
    #dealer draw until > 16
    #NOTES:
        #currently just one deck. 
        #will not be handlign splits for MVP. (that will come on the next round)
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# Card Values
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,  # typically, Ace's value is 11 unless it would cause the player's hand to bust, then it's 1.
}

# 4 suits
suits = ['hearts', 'diamonds', 'clubs', 'spades']

deck = {}

# Iterate over suits and values to fill the deck
for suit in suits:
    for value in values.keys():
        # Using the suit and value as the key for readability
        # If you want to add images or more info later, you can change the 2nd part of the dict to another dict or a class instance
        card_key = f'{value} of {suit}'
        deck[card_key] = values[value]


def draw_a_card():
    #Draw a random card
    card = random.choice(list(deck.keys()))
    #Get the cards value
    card_value = deck[card]
    return [card, card_value]


# print(deck)

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'

if play:
    player_card_1 = draw_a_card()
    player_card_2 = draw_a_card()
    players_cards = [];
    players_cards.extend([player_card_1, player_card_2])
    dealers_card_1 = draw_a_card()
    dealers_card_2 = draw_a_card()
    dealers_cards = []
    dealers_cards.extend([dealers_card_1, dealers_card_2])
    print(logo)
    print(players_cards)
    print(dealers_card_1)


