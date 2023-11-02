cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
card_values = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12,
               'SK': 13, 'SA': 14}


# If the cards passed in are three cards in a sequence, this function returns the greatest value.
def check_straight(card1, card2, card3):
    # global card_values
    # On line 12 making a list called values
    values = [card_values[card1], card_values[card2], card_values[card3]]
    values.sort()
    # since the values are sorted the greatest value will be at index 2 (card3)
    if values[1] == values[0] + 1 and values[2] == values[1] + 1:
        return values[2]
    else:
        return 0


# print(check_straight('S5', 'S6', 'S7'))
# print(check_straight('SJ', 'S8', 'S2'))

# If the three cards passed in are all the same, return the value. Otherwise return 0.
def check_3ofa_kind(card1, card2, card3):
    values = [card_values[card1], card_values[card2], card_values[card3]]
    if values[0] == values[1] and values[1] == values[2] and values[2] == values[1]:
        return values[0]
    else:
        return 0


# print(check_3ofa_kind('S7', 'S9', 'S8'))
# print(check_3ofa_kind('S7', 'S7', 'S7'))

# If the cards passed in are a straight with the value of 14, then this function returns 14.Otherwise, it will return 0.
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


# print(check_royal_flush('SQ', 'SK', 'SA'))


def play_cards(left1, left2, left3, right1, right2, right3):
    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)
    if left_3ofa_kind and right_3ofa_kind:
        return -1 if left_3ofa_kind > right_3ofa_kind else 1 if right_3ofa_kind > left_3ofa_kind else 0
    left_is_straight = check_straight(left1, left2, left3)
    right_is_straight = check_straight(right1, right2, right3)
    if left_is_straight and not right_is_straight:
        return -1
    if right_is_straight and not left_is_straight:
        return 1
    if left_is_straight and right_is_straight:
        return -1 if left_is_straight > right_is_straight else 1 if right_is_straight > left_is_straight else 0
    left_is_royal_flush = check_royal_flush(left1, left2, left3)
    right_is_royal_flush = check_royal_flush(right1, right2, right3)
    if left_is_royal_flush and not right_is_royal_flush:
        return -1
    if right_is_royal_flush and not left_is_royal_flush:
        return 1
    return 0
