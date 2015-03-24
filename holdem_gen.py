import itertools
from EvalHands import *
from Hand import *

# take out_cards as list and remove them from deck
def gen_deck_without_cards(out_cards):
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

def gen_player_cards(deck):
    return itertools.combinations(deck, 2)

def gen_board_cards(deck, board_len):
    return itertools.combinations(deck, 5 - board_len)

def gen_player_hands(board, player_cards):
    all_cards =list(board + player_cards)
    return itertools.combinations(all_cards, 5)

def gen_hand_cards(hand):
    cards = list(hand)
    cards_list = list()
    for card in cards:
        cards_list.append(card)
    return cards

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
                if hand1[i] > hand2.value_list[i]:
                    return hand1
                elif hand1.value_list[i] < hand2.value_list[i]:
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
            results = compair_hands(results, hand.hand_result())
        else:
            results = hand.hand_result()
    return results

def hand_mapping(*args):
    result_list = dict()
    for result in args:
        result_list.update(result)

    return sorted(result_list.item(), key = lambda t: t[0])




a = Card.Card('Td')
b = Card.Card('Ac')
c = Card.Card('Ad')
d = Card.Card('2h')
e = Card.Card('Th')
out_cards = list()
out_cards.extend([a,b,c,d,e])

f = Card.Card('2c')
g = Card.Card('3c')
p_hand = list()
p_hand.extend([f,g])
#out_cards = out_cards + p_hand
z = gen_deck_without_cards(out_cards)
results = list()
han = gen_player_hands(out_cards, p_hand)
for hand in han:
    x = gen_hand_cards(hand)
    xy = evalhands(hand)
    results.append(xy)
maoz = gen_result_list(results)
print maoz

