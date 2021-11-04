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


all_cards = []

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

print(all_cards)
print("\n")
random.shuffle(all_cards)
print(all_cards)
