# Programmers: Jonathan, Sebastian
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: Decision to draw another card or stay with given cards
# Program Outputs: Game outcome, deciding which player wins the round

import random


def generate_card_list(card_type):
    temp_list = []
    for i in range(1, 14):
        temp_list.append(str(i) + card_type)
    return temp_list


def str_cards_type(card_list, replace_letter, replace_message):
    card_type_list = []
    for i in card_list:
        new_string = i.replace(replace_letter, replace_message)
        card_type_list.append(new_string)
    return card_type_list


def ace_replace(card_list):
    ace_string = card_list[0].replace("1", "ace")
    card_list.insert(0, ace_string)
    card_list.pop(1)
    return card_list


def draw_cards(card_list, player_list, number_of_cards):
    i = 0
    while i < number_of_cards:
        player_list.append(card_list[i])
        i += 1
    for i in range(number_of_cards):
        card_list.pop(0)
    return player_list


def validate_input(message):
    is_valid = False
    return_message = None
    while not is_valid:
        choice = input(message)
        while not choice.isdigit():
            choice = input(message)
        choice = int(choice)
        is_valid = choice in range(1, 3)
        return_message = choice
    return return_message


def find_points(players_cards):
    total_points = 0
    for i in range(len(players_cards)):
        current_card = players_cards[i]
        if current_card[0] == "k" or current_card[0] == "q" or current_card[0] == "j":
            total_points += 10
        elif current_card[0] == "a":
            ace_choice = validate_input("What will this card be worth? 1 = one point, 2 = eleven points: ")
            if ace_choice == 1:
                total_points += 1
            elif ace_choice == 2:
                total_points += 11
        elif current_card[0] == "1":
            total_points += 10
        else:
            points = int(current_card[0])
            total_points += points
    return total_points


def main():
    all_cards = []
    dealer_cards = []
    player_cards = []

    club_cards_13 = ace_replace(str_cards_type(generate_card_list("c"), "c", " of clubs"))
    heart_cards_13 = ace_replace(str_cards_type(generate_card_list("h"), "h", " of hearts"))
    diamond_cards_13 = ace_replace(str_cards_type(generate_card_list("d"), "d", " of diamonds"))
    spade_cards_13 = ace_replace(str_cards_type(generate_card_list("s"), "s", " of spades"))

    all_cards.extend(club_cards_13)
    all_cards.extend(heart_cards_13)
    all_cards.extend(diamond_cards_13)
    all_cards.extend(spade_cards_13)

    all_cards = str_cards_type(all_cards, "13", "king")
    all_cards = str_cards_type(all_cards, "12", "queen")
    all_cards = str_cards_type(all_cards, "11", "jack")

    random.shuffle(all_cards)
    print(all_cards)
    print("\n")

    player_cards = draw_cards(all_cards, player_cards, 2)
    print(player_cards)
    player_points = find_points(player_cards)
    print("Player 1 current points: " + str(player_points))

    is_valid = False
    while player_points < 21 and not is_valid:
        hit_card = validate_input("\nWould you like to draw another card? 1 = yes, 2 = no: ")
        if hit_card == 1:
            new_card = all_cards[0]
            all_cards.pop(0)
            player_cards.append(new_card)
            print(player_cards)
            player_points = find_points(player_cards)
            print("Player 1 current points: " + str(player_points))
        elif hit_card == 2:
            print(player_cards)
            print("Player 1 Final Points: " + str(player_points))
            is_valid = True

    if player_points == 21:
        print("Player one has won, BlackJack!")
    elif player_points > 21:
        print("Player one has bust! :( ")
        exit()
    elif player_points < 21:
        print("\nDealers Turn!")



main()
