import itertools
from EvalHands import *
from Hand import *
import time
import random

# take out_cards as list and remove them from deck
def gen_deck_without_cards(hand, board=0):
    out_cards = list()
    if board != 0:
        out_cards.extend(board)
    out_cards.extend(hand)
    deck = []
    shaps = ['h', 'd', 'c', 's']
    val_string = "AKQJT98765432"

    for shap in shaps:
        for cardvalue in val_string:
            x = Card.Card(cardvalue + shap )
            deck.append(x)
    for out_card in out_cards:
        deck.remove(out_card)
    return tuple(deck)


# generate boards cards
def gen_board_cards(deck, board_len=0):
    random.seed(time.time())
    return random.sample(deck, 5 - board_len)

# can take 5,6,7 cards (boards + player cards), create hands
def gen_player_hands(board, player_cards):
    #all_cards =list()
    all_cards = board + player_cards
    #all_cards = tuple(all_cards)
    return itertools.combinations(all_cards, 5)

def gen_cards_from_hand(hand):
    cards = list(hand)
    cards_list = list()
    for card in cards:
        cards_list.append(card)
    return cards

def gen_opponent_cards(deck):
    random.seed(time.time())
    yield random.sample(deck, 2)

# takes two hands and return the winner
def compair_hands(hand1, hand2):
    result1 = hand1[0]
    result2 = hand2[0]
    if result1 > result2:
        return hand1
    if result1 < result2:
        return hand2
    if result1 == result2:
        if result1 == 1:
            for i in xrange(4,-1,-1):
                if hand1[2][i] > hand2[2][i]:
                    return hand1
                elif hand1[2][i] < hand2[2][i]:
                    return hand2
            return hand1
        #pair
        if result1 == 2:
            for i in xrange(2,6,1):
                if hand1[i] > hand2[i]:
                    return hand1
                elif hand1[i] < hand2[i]:
                    return hand2
            return hand1

        # two pairs and three
        if result1 in [3,4]:
            for i in xrange(2,5,1):
                if hand1[i] > hand2[i]:
                    return hand1
                elif hand1[i] < hand2[i]:
                    return hand2
            return hand1

        # Straight , flush, Straight flush
        if result1 in [5,6,9]:
            if hand1[-1] > hand2[-1]:
                return hand1
            elif hand1[-1] < hand2[-1]:
                return hand2
            return hand1

        # full house and four of a kind
        if result1 in [7,8]:
            for i in xrange(2,4,1):
                if hand1[i] > hand2[i]:
                    return hand1
                elif hand1[i] < hand2[i]:
                    return hand2
            return hand1


def gen_result_list(hands):
    results = None
    for hand in hands:
        if results is not None:
            hand_r = hand.hand_result()
            results = compair_hands(results, hand_r)
        else:
            results = hand.hand_result()
    return results

def hand_mapping(*args):
    result_list = dict()
    for result in args:
        result_list.update(result)

    return sorted(result_list.item(), key = lambda t: t[0])

def main_process(board, player_hand):
    result_list = list()
    all_hands = gen_player_hands(board, player_hand)
    for hand in all_hands:
        hand_result = evalhands(hand)
        result_list.append(hand_result)
    final_result = gen_result_list(result_list)
    return final_result


# a = Card.Card('Td')
# b = Card.Card('Ac')
# c = Card.Card('Ad')
# d = Card.Card('2h')
# e = Card.Card('Th')
# out_cards = list()
# out_cards.extend([a,b,c,d,e])
#
# f = Card.Card('2c')
# g = Card.Card('3c')
# p_hand = list()
# p_hand.extend([f,g])
# #out_cards = out_cards + p_hand
# z = gen_deck_without_cards(out_cards)
# results = list()
# han = gen_player_hands(out_cards, p_hand)
# for hand in han:
#     x = gen_cards_from_hand(hand)
#     xy = evalhands(hand)
#     results.append(xy)
# maoz = gen_result_list(results)
# print maoz

