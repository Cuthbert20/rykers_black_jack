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
        #not popping off card from deck that was drawn (simulates multipule decks)
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
    player_score = sum(card[1] for card in players_cards)
    dealers_score = sum(card[1] for card in dealers_cards)
    print(logo)
    print(f"Your cards are: {players_cards} your current score is: {player_score}")
    print(dealers_card_1)
    draw_again = input("type 'y' to get another card, type 'n' to pass: ").lower() == 'y'
    while draw_again and player_score < 21:
        players_card = draw_a_card()
        players_cards.append(players_card)
        player_score += players_card[1]
        print(f"Your cards are: {players_cards}, current score: {player_score}")   
        if player_score == 21:
            # print("BlackJack, you win  \U0001F929")
            break
        elif player_score > 21:
            # print("you loose, well lets see if the dealer busted")
            break
        draw_again = input("type 'y' to get another card, type 'n' to pass: ").lower() == 'y'
#now we are out of our loop, we need to check the dealers score and they will pull til they hit a number >=16
while dealers_score < 16:
    dealers_card = draw_a_card()
    dealers_score += dealers_card[1]
#lose conditions.    
if player_score > 21 or (dealers_score <= 21 and dealers_score > player_score):
    print(f"You loose Player Score: {player_score}, Dealer Score: {dealers_score}")
elif dealers_score == player_score and player_score <= 21:
    print("We have a push")
else:
    print(f"You won, Player Score: {player_score}, Dealer Score: {dealers_score}")
## Still need to handle 11 or 1.

