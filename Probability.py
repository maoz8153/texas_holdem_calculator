import holdem_gen
import itertools

def cards_in_play(board, hand):
    card_in_play = list()
    card_in_play.extend(board)
    card_in_play.extend(hand)
    return cards_in_play

def deck_information(deck):
    num_suit_cards = [0]*4
    num_value_cards = [0]*13
    for card in deck:
        num_value_cards[14 - card.value] += 1
        num_suit_cards[card.suit_index] += 1
    return (num_suit_cards, num_value_cards)

def cards_valus_list(cards):
    values = list()
    for card in cards:
        values.append(card.value)
    values.sort()
    return values

def value_probabilty(deck):
     return [(14 - index, frequency) for index, frequency in enumerate(deck) if frequency]


# take any board given(3,4) plus hand and check if flush available and return the cards by frequency
def flush_available(board, hand):
    suits = dict()
    cards_in_play = list()
    cards_in_play.extend(board)
    cards_in_play.extend(hand)
    for card in cards_in_play:
        if card.suit_index in suits:
            suits[card.suit_index] += 1
        else:
            suits[card.suit_index] == 1

    suits = sorted(suits.items(), key=lambda x: x[1], reverse=True)
    if len(cards_in_play) == 5 and suits[0][1] > 2:
        return {suits[0][0] : suits[0][1]}
    elif len(cards_in_play) == 6 and suits[0][1] > 3:
        return {suits[0][0] : suits[0][1]}
    else:
        return None

def flot_probabilty(board, hand):
    current_hand = holdem_gen.main_process(board, hand)
    out_cards = list()
    out_cards.extend(board)
    out_cards.extend(hand)
    deck = holdem_gen.gen_deck_without_cards(out_cards)

def flush_probabilty(board, hand):
    is_flush = flush_available(board,hand)
    if is_flush is not None:
        deck = holdem_gen.gen_deck_without_cards(board,hand)
        suit_cards, values_cards  = deck_information(deck)
        number_of_cards = 5 - is_flush[0][0]
        if number_of_cards == 2 :
            prob = suit_cards[is_flush[0][0]]*(suit_cards[is_flush[0][0]] - 1)/float(len(deck)* (len(deck) - 1))
        if number_of_cards == 1:
            prob = suit_cards[is_flush[0][0]]/float(len(deck))
        return prob
    else:
        return 0

def ace_in_cards_list(cards_list):
    new_cards_list = []
    if 14 in cards_list:
        new_cards_list[0].append(cards_list)
        cards_list.pop[-1]
        cards_list.extend(1)
        cards_list.sort()
        new_cards_list[1].append(cards_list)
        return new_cards_list
    else:
        return cards_list

# check if straight available and if so return cards needed
def straight_available(board, deck):
    cards = cards_in_play(board, deck)
    cards_list_before = cards_valus_list(cards)
    cards_list_after = ace_in_cards_list(cards_list_before)
    cards_needed = []
    for ii in xrange(len(cards_list_after)):
        cards_list = cards_list_after[ii]
        if len(cards_list) == 5:
            for i in xrange(0,3):
                delta = cards_list[i+2] - cards_list[i]
                if delta == 2 and cards_list[i+1] == cards_list[i] + 1:
                    if cards_list[0] != 1:
                        if cards_list[i+3] - cards_list[i] == 3:
                            cards_needed = list([cards_list[i+2] + 2], [cards_list[i] - 1])
                        else:
                            cards_needed = list([cards_list[i+2] + 1, cards_list[i+2] + 2], [cards_list[i] - 1, cards_list[i] - 2])
                    else:
                        if cards_list[i+3] - cards_list[i] == 3:
                            cards_needed = list([cards_list[i+2] + 2])
                        else:
                            cards_needed = list([cards_list[i+2] + 1, cards_list[i+2] + 2])

                if 2 < delta <= 4 :
                    if cards_list[i+1] in (cards_list[i]+1,cards_list[i]+2):
                        xcards = set(cards_list[i]+1,cards_list[i]+2) - set(cards_list[i+1])
                        if cards_list[i+3] - cards_list[i] == 3:
                            cards_needed = list(xcards)
                        else:
                            cards_needed = list(xcards, cards_list[i+2] + 1)

        elif len(cards_list) == 6:
            for i in xrange(0,3):
                delta = cards_list[i+3] - cards_list[i]
                if delta == 3:
                    test_delta = True
                    for iii in xrange(0,3):
                        if cards_list[iii+1] - cards_list[iii] != 1:
                            test_delta = False
                    if test_delta:
                        cards_needed = list([cards_list[i]-1, cards_list[i+3]+1])
                if delta == 4:
                    xcards = set(list(range(cards_list[i],cards_list[i+3]))) - set(cards_list[i:i+3])
                    if len(xcards) == 1:
                        cards_needed = list(xcards)

    if len(cards_needed) > 0:
        return cards_needed
    else:
        return None










# def __init__(self, hand, deck, board):
#     self.number_of_cards = len(hand.cards)
#     self.num_board_cards = len(board.cards)
#     self.cards_left = len(deck.cards) - self.number_of_cards - self.num_board_cards
#     self.pro_shap_list = hand.shap_list + board.shap_list
#     self.pro_value_list = hand.value_list + board.value_list
#     self.grop = ''


    # if self.num_board_cards > 0 :
    #     self.shap_list = hand.shap_list + board.shap_list
    #     self.value_list = hand.value_list + board.value_list
    # else:
    #    self.shap_list = hand.shap_list
    #    self.value_list = hand.value_list

# def suit(self):
#     if self.shap_list[0] == self.shap_list[1]:
#         return True
#
# def group_prob(self):
#     gap = 0
#     if self.value_list[0] == self.value_list[1]:
#         self.grop = 'pocket_pair'
#     else:
#         if '1' in self.value_list:
#             gap = abs(self.value_list[0] - self.value_list[1])
#             if gap > 4:
#                 for index, val in enumerate(self.value_list):
#                     if val == '1':
#                         self.value_list[index] == '14'
#                         break
#                 gap = abs(self.value_list[0] - self.value_list[1])









