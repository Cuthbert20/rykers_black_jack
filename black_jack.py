#blackJack Game.
#Rykers Thoughts on building our game.
    #build a deck
    #have a system to grab random cards.
    #deal cards.
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
        
print(deck)

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'

if play:
    print(logo)

