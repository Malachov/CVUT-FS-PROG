#Github token: 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

from Classes import Game, Round, Card, Player

# enter the number of players
num_of_players_OK = False
while (num_of_players_OK == False):
    try:
        num_of_players = int(input("How many players? "))
        num_of_players_OK = True
    except ValueError:
        print("Your should enter a number. Please enter the integer datatype")

# initiate the game
game1 = Game(num_of_players)
# create deck of cards
game1.create_deck_of_cards()
# instantiate players
game1.create_players()

rounds_played = [] # For saving rounds which have been played

while game1.num_of_rounds < 2:
    game1.num_of_rounds += 1
    current_round = Round()

    # deal cards
    current_round.deal_cards(game1)

    # print out the cards held by the first player
    # this is for the case when cards are defined as tuples
    # print(f"{game1.players[1].name} has these cards: {game1.players[0].cards_in_hand} .")
    # this is for the case when cards are defined as instances of Card class
    print(f"{game1.players[0].name} has these cards: ", game1.players[0].display_cards_in_hand())

    # Choose the player who will start the round
    first_player_index = current_round.choose_first_player(game1)

    # Every player chooses their card for the current round

    for i in range(len(game1.players)):
        played_card = game1.players[first_player_index-i].choose_card()
        current_round.played_cards.append(played_card)
        print(current_round.display_played_cards_in_round()) # Prints out currently played cards

    # End of a round
    print(f"{game1.num_of_rounds}. round is finished")

    rounds_played.append(current_round) # Saving played rounds into a list


print(rounds_played)